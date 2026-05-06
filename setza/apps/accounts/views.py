from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from pydantic import ValidationError

from apps.common.validation import pydantic_errors

from .mappers import AUTH_FORM_FIELDS, ForgotPasswordInput, SignInInput, SignUpInput, form_values
from .models import Role, User


def _dashboard_url_for(user):
    if user.active_role == "brand":
        return "brand:dashboard"
    return "creator:dashboard"


class AuthFormView(TemplateView):
    form_name = ""
    page_title = ""
    page_description = ""
    submit_label = ""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.form_name in {"sign_in", "sign_up"}:
            return redirect(_dashboard_url_for(request.user))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("form_name", self.form_name)
        context.setdefault("page_title", self.page_title)
        context.setdefault("page_description", self.page_description)
        context.setdefault("submit_label", self.submit_label)
        context.setdefault("fields", AUTH_FORM_FIELDS[self.form_name])
        context.setdefault("values", form_values({}, self.form_name))
        context.setdefault("field_errors", {})
        context.setdefault("non_field_errors", [])
        if self.form_name == "sign_in":
            context.setdefault(
                "demo_accounts",
                [
                    {"label": "Creator Demo", "email": "creator@setza.com", "password": "demo1234"},
                    {"label": "Brand Demo", "email": "brand@setza.com", "password": "demo1234"},
                ],
            )
        return context

    def render_form(self, payload=None, field_errors=None, non_field_errors=None, status=200):
        context = self.get_context_data(
            values=form_values(payload, self.form_name),
            field_errors=field_errors or {},
            non_field_errors=non_field_errors or [],
        )
        return self.render_to_response(context, status=status)


class SignInView(AuthFormView):
    template_name = "pages/auth/sign_in.html"
    form_name = "sign_in"
    page_title = "Sign In"
    page_description = "Use your Setza account first. Social platforms connect after you are inside."
    submit_label = "Sign In"

    def post(self, request, *args, **kwargs):
        payload = request.POST.dict()
        try:
            mapper = SignInInput.model_validate(payload)
        except ValidationError as exc:
            field_errors, non_field_errors = pydantic_errors(exc)
            return self.render_form(payload, field_errors, non_field_errors, status=400)

        user = authenticate(request, email=mapper.email, password=mapper.password)
        if not user:
            return self.render_form(payload, non_field_errors=["Invalid email or password."], status=400)

        login(self.request, user)
        return redirect(_dashboard_url_for(user))


class SignUpView(AuthFormView):
    template_name = "pages/auth/sign_up.html"
    form_name = "sign_up"
    page_title = "Create Account"
    page_description = "Build your Setza identity first, then connect Instagram, TikTok, and YouTube."
    submit_label = "Create Setza Account"

    def post(self, request, *args, **kwargs):
        payload = request.POST.dict()
        try:
            mapper = SignUpInput.model_validate(payload)
        except ValidationError as exc:
            field_errors, non_field_errors = pydantic_errors(exc)
            return self.render_form(payload, field_errors, non_field_errors, status=400)

        if User.objects.filter(email__iexact=mapper.email).exists():
            return self.render_form(payload, field_errors={"email": ["An account with this email already exists."]}, status=400)

        with transaction.atomic():
            user = User.objects.create_user(
                email=mapper.email,
                password=mapper.password,
                username=mapper.email.split("@")[0],
                active_role=mapper.role,
            )
            Role.objects.get_or_create(user=user, role=mapper.role, defaults={"is_primary": True})

        login(self.request, user, backend=settings.AUTHENTICATION_BACKENDS[0])
        return redirect("onboarding:role")


class ForgotPasswordView(AuthFormView):
    template_name = "pages/auth/forgot_password.html"
    form_name = "forgot_password"
    page_title = "Forgot Password"
    page_description = "We will prepare reset instructions for the email you enter in this local demo flow."
    submit_label = "Send Reset Link"

    def post(self, request, *args, **kwargs):
        payload = request.POST.dict()
        try:
            ForgotPasswordInput.model_validate(payload)
        except ValidationError as exc:
            field_errors, non_field_errors = pydantic_errors(exc)
            return self.render_form(payload, field_errors, non_field_errors, status=400)

        messages.success(self.request, "Password reset instructions were prepared for this demo flow.")
        return redirect(reverse_lazy("accounts:sign_in"))


class SignOutView(LogoutView):
    next_page = reverse_lazy("accounts:sign_in")

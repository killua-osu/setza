from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView
from pydantic import ValidationError

from apps.common.mock_data import get_connected_accounts
from apps.common.validation import pydantic_errors

from .mappers import BasicProfileInput, RoleSelectionInput


class RoleSelectionView(LoginRequiredMixin, TemplateView):
    template_name = "pages/onboarding/role.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("field_errors", {})
        context.setdefault("non_field_errors", [])
        return context

    def post(self, request, *args, **kwargs):
        try:
            mapper = RoleSelectionInput.model_validate(request.POST.dict())
        except ValidationError as exc:
            field_errors, non_field_errors = pydantic_errors(exc)
            context = self.get_context_data(field_errors=field_errors, non_field_errors=non_field_errors)
            return self.render_to_response(context, status=400)

        role = mapper.role
        if request.user.is_authenticated:
            request.user.active_role = role
            request.user.save(update_fields=["active_role"])
        request.session["setza_role"] = role
        return redirect("onboarding:connect_accounts")


class BasicProfileView(LoginRequiredMixin, TemplateView):
    template_name = "pages/onboarding/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("values", {})
        context.setdefault("field_errors", {})
        context.setdefault("non_field_errors", [])
        return context

    def post(self, request, *args, **kwargs):
        payload = request.POST.dict()
        try:
            mapper = BasicProfileInput.model_validate(payload)
        except ValidationError as exc:
            field_errors, non_field_errors = pydantic_errors(exc)
            context = self.get_context_data(values=payload, field_errors=field_errors, non_field_errors=non_field_errors)
            return self.render_to_response(context, status=400)

        request.session["setza_onboarding_profile"] = mapper.model_dump()
        messages.success(request, "Basic profile details saved for the onboarding demo.")
        return redirect("onboarding:connect_accounts")


class ConnectAccountsView(LoginRequiredMixin, TemplateView):
    template_name = "pages/onboarding/connect_accounts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["connected_accounts"] = get_connected_accounts()
        context["current_role"] = self.request.session.get("setza_role", "creator")
        return context

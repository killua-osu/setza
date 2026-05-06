from django.urls import path

from .views import ForgotPasswordView, SignInView, SignOutView, SignUpView

app_name = "accounts"

urlpatterns = [
    path("sign-in/", SignInView.as_view(), name="sign_in"),
    path("sign-up/", SignUpView.as_view(), name="sign_up"),
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot_password"),
    path("sign-out/", SignOutView.as_view(), name="sign_out"),
]

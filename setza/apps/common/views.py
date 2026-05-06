from django.shortcuts import redirect
from django.views import View


class AppEntryRedirectView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("accounts:sign_in")
        if request.user.active_role == "brand":
            return redirect("brand:dashboard")
        return redirect("creator:dashboard")

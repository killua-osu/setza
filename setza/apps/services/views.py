from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView


class ServicesRedirectView(LoginRequiredMixin, RedirectView):
    pattern_name = "creator:services"
    permanent = False

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .services import build_layout_context


class SetzaPageMixin(LoginRequiredMixin, TemplateView):
    role = "creator"
    active_nav = "dashboard"
    active_sidebar = None
    switch_kwargs = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            build_layout_context(
                self.request,
                role=self.role,
                active_nav=self.active_nav,
                active_sidebar=self.active_sidebar,
                switch_kwargs=self.get_switch_kwargs(),
            )
        )
        return context

    def get_switch_kwargs(self):
        return self.switch_kwargs or {}

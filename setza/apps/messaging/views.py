from copy import deepcopy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import RedirectView
from pydantic import ValidationError

from apps.common.mock_data import get_messages
from apps.common.validation import pydantic_errors
from apps.common.viewmixins import SetzaPageMixin

from .mappers import MessageReplyInput, ThreadSelectionInput


def _merged_conversation(request, role, slug):
    messaging = get_messages(role)
    conversations = messaging["conversations"]
    active = next((item for item in conversations if item["slug"] == slug), conversations[0])
    active = deepcopy(active)
    extra = request.session.get("setza_messages", {}).get(f"{role}:{slug}", [])
    active["messages"].extend(extra)
    return messaging, active


class BaseMessagesPage(SetzaPageMixin):
    active_nav = "dashboard"
    active_sidebar = "messages"
    template_name = "pages/messages/inbox.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messaging = get_messages(self.role)
        active_slug = ThreadSelectionInput.model_validate(self.request.GET.dict()).thread or messaging["conversations"][0]["slug"]
        messaging, active = _merged_conversation(self.request, self.role, active_slug)
        context["messaging"] = messaging
        context["active_slug"] = active_slug
        context["active_conversation"] = active
        return context


class CreatorMessagesView(BaseMessagesPage):
    role = "creator"


class BrandMessagesView(BaseMessagesPage):
    role = "brand"


class ThreadPartialView(LoginRequiredMixin, View):
    def get(self, request, role, slug):
        messaging, active = _merged_conversation(request, role, slug)
        return render(
            request,
            "components/chat_window.html",
            {
                "current_role": role,
                "messaging": messaging,
                "active_slug": slug,
                "active_conversation": active,
            },
        )


class SendMessageView(LoginRequiredMixin, View):
    def post(self, request, role, slug):
        try:
            mapper = MessageReplyInput.model_validate(request.POST.dict())
        except ValidationError as exc:
            field_errors, non_field_errors = pydantic_errors(exc)
            message = (field_errors.get("body") or non_field_errors or ["Missing message body."])[0]
            return HttpResponseBadRequest(message)

        session_messages = request.session.setdefault("setza_messages", {})
        key = f"{role}:{slug}"
        session_messages.setdefault(key, []).append({"sender": "me", "time": "Just now", "body": mapper.body})
        request.session["setza_messages"] = session_messages
        request.session.modified = True
        messaging, active = _merged_conversation(request, role, slug)
        return render(
            request,
            "components/chat_window.html",
            {
                "current_role": role,
                "messaging": messaging,
                "active_slug": slug,
                "active_conversation": active,
            },
        )


class SharedMessagesRedirectView(LoginRequiredMixin, RedirectView):
    pattern_name = "creator:messages"
    permanent = False

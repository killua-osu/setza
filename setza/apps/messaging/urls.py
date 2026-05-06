from django.urls import path

from .views import SendMessageView, SharedMessagesRedirectView, ThreadPartialView

app_name = "messaging"

urlpatterns = [
    path("", SharedMessagesRedirectView.as_view(), name="root"),
    path("thread/<str:role>/<slug:slug>/", ThreadPartialView.as_view(), name="thread"),
    path("thread/<str:role>/<slug:slug>/send/", SendMessageView.as_view(), name="send"),
]

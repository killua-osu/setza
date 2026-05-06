from django.contrib import admin

from .models import Conversation, Message


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("topic_label", "topic_type", "creator_profile", "brand_profile", "last_message_at")
    list_filter = ("topic_type",)
    search_fields = ("topic_label",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("conversation", "sender", "created_at", "is_read")
    list_filter = ("is_read", "is_system")

# Register your models here.

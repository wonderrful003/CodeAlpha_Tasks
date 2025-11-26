from django.contrib import admin
from .models import FAQ, ChatSession, ChatMessage

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['question', 'answer']

@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ['session_id', 'created_at']
    readonly_fields = ['session_id', 'created_at', 'updated_at']

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['session', 'message_short', 'is_user', 'confidence', 'timestamp']
    list_filter = ['is_user', 'timestamp']
    readonly_fields = ['timestamp']
    
    def message_short(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    message_short.short_description = 'Message'
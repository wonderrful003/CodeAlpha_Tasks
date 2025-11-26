from django.db import models
import uuid

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.question[:50] + "..." if len(self.question) > 50 else self.question

class ChatSession(models.Model):
    session_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Session {self.session_id}"

class ChatMessage(models.Model):
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    is_user = models.BooleanField(default=True)  # True for user, False for bot
    timestamp = models.DateTimeField(auto_now_add=True)
    confidence = models.FloatField(null=True, blank=True)  # AI confidence score
    
    def __str__(self):
        return f"{'User' if self.is_user else 'Bot'}: {self.message[:30]}"
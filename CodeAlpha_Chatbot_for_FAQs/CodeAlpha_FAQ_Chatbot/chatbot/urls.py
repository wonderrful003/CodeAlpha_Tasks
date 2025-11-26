from django.urls import path
from . import views
from django.http import HttpResponse

def show_urls(request):
    """Show all available URLs"""
    urls = [
        "<h1>Available URLs:</h1>",
        "<ul>",
        "<li><a href='/'>/ - Main Chat</a></li>",
        "<li><a href='/faqs/'>/faqs/ - FAQ Management</a></li>", 
        "<li><a href='/api/chat/'>/api/chat/ - Chat API</a></li>",
        "<li><a href='/admin/'>/admin/ - Django Admin</a></li>",
        "</ul>"
    ]
    return HttpResponse("".join(urls))

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('api/chat/', views.get_bot_response, name='get_bot_response'),
    path('faqs/', views.faq_management, name='faq_management'),
    path('urls/', show_urls, name='show_urls'),  # Add this for debugging
]
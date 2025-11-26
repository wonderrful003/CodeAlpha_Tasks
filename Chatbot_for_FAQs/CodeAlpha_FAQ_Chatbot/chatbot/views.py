from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import uuid
from .models import ChatSession, ChatMessage, FAQ
from .utils import chatbot

def chat_view(request):
    """Main chat interface"""
    session_id = request.session.get('chat_session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        request.session['chat_session_id'] = session_id
        ChatSession.objects.get_or_create(session_id=session_id)
    
    # Auto-train chatbot if not trained
    if not chatbot.is_trained and FAQ.objects.exists():
        print("🔄 Auto-training chatbot...")
        chatbot.train()
    
    return render(request, 'chatbot/chat.html')

@csrf_exempt
def get_bot_response(request):
    """API endpoint to get bot response"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            user_message = data.get('message', '').strip()
            session_id = request.session.get('chat_session_id')
            
            print(f"💬 User message: '{user_message}'")
            
            if not user_message:
                return JsonResponse({'error': 'Empty message'}, status=400)
            
            # Get AI response
            bot_response, confidence = chatbot.get_response(user_message)
            print(f"🤖 Bot response: '{bot_response}'")
            print(f"📈 Confidence: {confidence}")
            
            # Save to database
            if session_id:
                try:
                    session, created = ChatSession.objects.get_or_create(session_id=session_id)
                    
                    ChatMessage.objects.create(
                        session=session,
                        message=user_message,
                        is_user=True
                    )
                    
                    ChatMessage.objects.create(
                        session=session,
                        message=bot_response,
                        is_user=False,
                        confidence=confidence
                    )
                    
                except Exception as e:
                    print(f"❌ Error saving to database: {e}")
            
            return JsonResponse({
                'response': bot_response,
                'confidence': round(confidence, 2)
            })
            
        except Exception as e:
            print(f"❌ Error in get_bot_response: {e}")
            import traceback
            traceback.print_exc()
            return JsonResponse({
                'error': f'Server error: {str(e)}'
            }, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def faq_management(request):
    """FAQ management page"""
    if request.method == 'POST':
        question = request.POST.get('question', '').strip()
        answer = request.POST.get('answer', '').strip()
        category = request.POST.get('category', 'General').strip()
        
        if question and answer:
            FAQ.objects.create(
                question=question,
                answer=answer,
                category=category
            )
            # Retrain chatbot with new FAQs
            print("🔄 Retraining chatbot with new FAQs...")
            chatbot.train()
            return redirect('faq_management')
    
    faqs = FAQ.objects.all().order_by('-created_at')
    return render(request, 'chatbot/faq_management.html', {
        'faqs': faqs,
        'faq_count': faqs.count()
    })
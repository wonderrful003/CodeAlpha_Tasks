from django.core.management.base import BaseCommand
from chatbot.models import FAQ

class Command(BaseCommand):
    help = 'Load sample FAQ data into the database'

    def handle(self, *args, **options):
        sample_faqs = [
            {
                'question': 'What is your return policy?',
                'answer': 'We offer a 30-day return policy for all unused items in original packaging with receipt.',
                'category': 'Returns'
            },
            {
                'question': 'How long does shipping take?',
                'answer': 'Standard shipping takes 5-7 business days. Express shipping (2-3 days) is also available.',
                'category': 'Shipping'
            },
            {
                'question': 'What payment methods do you accept?',
                'answer': 'We accept all major credit cards, PayPal, Apple Pay, and Google Pay.',
                'category': 'Payment'
            },
            {
                'question': 'Do you offer international shipping?',
                'answer': 'Yes, we ship to over 50 countries worldwide. International shipping takes 7-14 business days.',
                'category': 'Shipping'
            },
            {
                'question': 'How can I track my order?',
                'answer': 'You will receive a tracking number via email once your order ships. You can track it on our website.',
                'category': 'Orders'
            },
            {
                'question': 'What is your warranty policy?',
                'answer': 'We offer a 1-year warranty on all products. Contact support for warranty claims.',
                'category': 'Warranty'
            },
            {
                'question': 'Can I change my order after placing it?',
                'answer': 'You can modify your order within 1 hour of placement by contacting customer service.',
                'category': 'Orders'
            },
            {
                'question': 'Do you have a physical store?',
                'answer': 'Yes, we have stores in major cities. Check our website for locations near you.',
                'category': 'Stores'
            },
            {
                'question': 'How do I contact customer service?',
                'answer': 'You can reach us at support@company.com or call 1-800-123-4567 from 9 AM to 6 PM EST.',
                'category': 'Contact'
            },
            {
                'question': 'Are your products authentic?',
                'answer': 'Yes, we only sell 100% authentic products from authorized distributors.',
                'category': 'Products'
            }
        ]

        for faq_data in sample_faqs:
            FAQ.objects.get_or_create(
                question=faq_data['question'],
                defaults={
                    'answer': faq_data['answer'],
                    'category': faq_data['category']
                }
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully loaded sample FAQs!')
        )
from django.core.management.base import BaseCommand
from chatbot.models import FAQ

class Command(BaseCommand):
    help = 'Load comprehensive FAQ dataset for AI training'

    def handle(self, *args, **options):
        comprehensive_faqs = [
            # Shipping & Delivery (15 FAQs)
            {
                'question': 'How long does standard shipping take?',
                'answer': 'Standard shipping typically takes 5-7 business days for delivery.',
                'category': 'Shipping'
            },
            {
                'question': 'What is express shipping delivery time?',
                'answer': 'Express shipping delivers within 2-3 business days for most locations.',
                'category': 'Shipping'
            },
            {
                'question': 'Do you offer overnight shipping?',
                'answer': 'Yes, we offer overnight shipping for orders placed before 2 PM EST.',
                'category': 'Shipping'
            },
            {
                'question': 'What are your shipping costs?',
                'answer': 'Standard shipping is $4.99, express is $9.99, and overnight is $19.99. Free shipping on orders over $50.',
                'category': 'Shipping'
            },
            {
                'question': 'Do you ship internationally?',
                'answer': 'Yes, we ship to over 100 countries worldwide with varying delivery times and costs.',
                'category': 'Shipping'
            },
            {
                'question': 'How can I track my order?',
                'answer': 'You can track your order using the tracking number sent to your email or in your account dashboard.',
                'category': 'Shipping'
            },
            {
                'question': 'What shipping carriers do you use?',
                'answer': 'We use USPS, FedEx, and UPS depending on your location and shipping method selected.',
                'category': 'Shipping'
            },
            {
                'question': 'Can I change my shipping address after ordering?',
                'answer': 'You can change your shipping address within 1 hour of placing your order by contacting customer service.',
                'category': 'Shipping'
            },
            {
                'question': 'Do you ship to PO boxes?',
                'answer': 'Yes, we ship to PO boxes via USPS for standard shipping methods.',
                'category': 'Shipping'
            },
            {
                'question': 'What is your processing time before shipping?',
                'answer': 'Orders are processed within 24-48 hours during business days before being shipped.',
                'category': 'Shipping'
            },
            {
                'question': 'Do you offer free shipping?',
                'answer': 'Yes, we offer free standard shipping on all orders over $50.',
                'category': 'Shipping'
            },
            {
                'question': 'Can I upgrade my shipping after ordering?',
                'answer': 'Shipping upgrades are possible within 2 hours of ordering by contacting our support team.',
                'category': 'Shipping'
            },
            {
                'question': 'What happens if my package is lost?',
                'answer': 'We investigate lost packages with the carrier and will reship or refund based on the investigation results.',
                'category': 'Shipping'
            },
            {
                'question': 'Do you offer same-day delivery?',
                'answer': 'Same-day delivery is available in select metropolitan areas for an additional fee.',
                'category': 'Shipping'
            },
            {
                'question': 'What are your shipping cut-off times?',
                'answer': 'Orders placed before 2 PM EST ship same day on business days.',
                'category': 'Shipping'
            },

            # Returns & Refunds (12 FAQs)
            {
                'question': 'What is your return policy?',
                'answer': 'We offer a 30-day return policy for unused items in original packaging with receipt.',
                'category': 'Returns'
            },
            {
                'question': 'How do I return an item?',
                'answer': 'Initiate returns through your account page or contact customer service for a return label.',
                'category': 'Returns'
            },
            {
                'question': 'Are return shipping costs covered?',
                'answer': 'We provide free return shipping for defective items or our errors. Otherwise, return shipping is customer responsibility.',
                'category': 'Returns'
            },
            {
                'question': 'How long do refunds take to process?',
                'answer': 'Refunds are processed within 3-5 business days after we receive your return.',
                'category': 'Returns'
            },
            {
                'question': 'Can I return opened items?',
                'answer': 'Opened items can be returned within 14 days if defective or not as described.',
                'category': 'Returns'
            },
            {
                'question': 'Do you offer exchanges?',
                'answer': 'Yes, we offer exchanges for size or color variations subject to availability.',
                'category': 'Returns'
            },
            {
                'question': 'What items are non-returnable?',
                'answer': 'Personal care items, underwear, and customized products are non-returnable for hygiene reasons.',
                'category': 'Returns'
            },
            {
                'question': 'Can I return sale items?',
                'answer': 'Sale items can be returned within 14 days with original tags and packaging.',
                'category': 'Returns'
            },
            {
                'question': 'How will I receive my refund?',
                'answer': 'Refunds are issued to your original payment method within 5-10 business days.',
                'category': 'Returns'
            },
            {
                'question': 'What if I receive a damaged item?',
                'answer': 'Contact us within 48 hours of delivery with photos for immediate replacement or refund.',
                'category': 'Returns'
            },
            {
                'question': 'Can I return gifts?',
                'answer': 'Gifts can be returned with gift receipt within 30 days for store credit.',
                'category': 'Returns'
            },
            {
                'question': 'Do you offer store credit?',
                'answer': 'Yes, store credit is available for returns without original receipt or after 30 days.',
                'category': 'Returns'
            },

            # Payment & Pricing (10 FAQs)
            {
                'question': 'What payment methods do you accept?',
                'answer': 'We accept Visa, MasterCard, American Express, PayPal, Apple Pay, Google Pay, and shop Pay.',
                'category': 'Payment'
            },
            {
                'question': 'Is my payment information secure?',
                'answer': 'Yes, we use SSL encryption and PCI-compliant payment processors to protect your information.',
                'category': 'Payment'
            },
            {
                'question': 'Do you offer payment plans?',
                'answer': 'Yes, we offer installment plans through PayPal Credit, Affirm, and Klarna for orders over $100.',
                'category': 'Payment'
            },
            {
                'question': 'Can I pay with multiple payment methods?',
                'answer': 'Yes, you can split payment between gift card and credit card during checkout.',
                'category': 'Payment'
            },
            {
                'question': 'Do you charge sales tax?',
                'answer': 'Sales tax is applied based on your shipping address and local tax regulations.',
                'category': 'Payment'
            },
            {
                'question': 'What currencies do you accept?',
                'answer': 'We accept USD, CAD, EUR, GBP, and AUD for international orders.',
                'category': 'Payment'
            },
            {
                'question': 'Can I use gift cards with other promotions?',
                'answer': 'Gift cards can be combined with most promotions unless otherwise stated.',
                'category': 'Payment'
            },
            {
                'question': 'Do you offer price matching?',
                'answer': 'We offer price matching within 14 days of purchase for identical items from authorized retailers.',
                'category': 'Payment'
            },
            {
                'question': 'What is your price adjustment policy?',
                'answer': 'We offer price adjustments within 7 days if an item goes on sale after your purchase.',
                'category': 'Payment'
            },
            {
                'question': 'Are there any hidden fees?',
                'answer': 'No hidden fees. You see the final total including tax and shipping before payment.',
                'category': 'Payment'
            },

            # Product & Inventory (10 FAQs)
            {
                'question': 'Are your products authentic?',
                'answer': 'Yes, we only sell 100% authentic products directly from manufacturers or authorized distributors.',
                'category': 'Products'
            },
            {
                'question': 'Do you have this item in stock?',
                'answer': 'Our website shows real-time inventory. If you can add to cart, it is in stock.',
                'category': 'Products'
            },
            {
                'question': 'Can I get notified when an item restocks?',
                'answer': 'Yes, click "Notify Me" on any out-of-stock product page to receive restock alerts.',
                'category': 'Products'
            },
            {
                'question': 'Do you offer product samples?',
                'answer': 'We offer samples for certain product categories. Check individual product pages for sample availability.',
                'category': 'Products'
            },
            {
                'question': 'What is your product sourcing?',
                'answer': 'We source directly from manufacturers and authorized distributors to ensure quality and authenticity.',
                'category': 'Products'
            },
            {
                'question': 'Do you test your products?',
                'answer': 'Yes, we conduct quality control tests on all products before they are listed for sale.',
                'category': 'Products'
            },
            {
                'question': 'Can I request a specific product?',
                'answer': 'Yes, you can submit product requests through our customer service team.',
                'category': 'Products'
            },
            {
                'question': 'Are your products eco-friendly?',
                'answer': 'We prioritize eco-friendly products and sustainable packaging whenever possible.',
                'category': 'Products'
            },
            {
                'question': 'Do you offer product customization?',
                'answer': 'Customization is available for select products. Check product pages for customization options.',
                'category': 'Products'
            },
            {
                'question': 'What is your product warranty?',
                'answer': 'Most products come with a 1-year manufacturer warranty. Check individual product pages for details.',
                'category': 'Products'
            },

            # Account & Technical (10 FAQs)
            {
                'question': 'How do I create an account?',
                'answer': 'Click "Sign Up" in the top right corner and follow the registration process.',
                'category': 'Account'
            },
            {
                'question': 'How do I reset my password?',
                'answer': 'Click "Forgot Password" on the login page and follow the email instructions.',
                'category': 'Account'
            },
            {
                'question': 'Can I change my email address?',
                'answer': 'Yes, you can update your email address in your account settings.',
                'category': 'Account'
            },
            {
                'question': 'How do I update my billing information?',
                'answer': 'Update billing information in your account under "Payment Methods" section.',
                'category': 'Account'
            },
            {
                'question': 'Can I delete my account?',
                'answer': 'Yes, you can request account deletion through your account settings or contact support.',
                'category': 'Account'
            },
            {
                'question': 'How do I view my order history?',
                'answer': 'Your complete order history is available in your account dashboard.',
                'category': 'Account'
            },
            {
                'question': 'Can I save multiple addresses?',
                'answer': 'Yes, you can save multiple shipping addresses in your address book.',
                'category': 'Account'
            },
            {
                'question': 'How do I update my communication preferences?',
                'answer': 'Manage email and notification preferences in your account settings.',
                'category': 'Account'
            },
            {
                'question': 'Is my personal data secure?',
                'answer': 'We use industry-standard encryption and never sell your personal data to third parties.',
                'category': 'Account'
            },
            {
                'question': 'Can I have multiple accounts?',
                'answer': 'Each customer should maintain only one account to ensure order history accuracy.',
                'category': 'Account'
            },

            # Customer Service (8 FAQs)
            {
                'question': 'How do I contact customer service?',
                'answer': 'Reach us at support@company.com, call 1-800-123-4567, or use our live chat from 9 AM to 9 PM EST.',
                'category': 'Support'
            },
            {
                'question': 'What are your customer service hours?',
                'answer': 'Our customer service team is available Monday to Friday, 9 AM to 9 PM EST.',
                'category': 'Support'
            },
            {
                'question': 'Do you have a live chat?',
                'answer': 'Yes, live chat is available on our website during business hours for immediate assistance.',
                'category': 'Support'
            },
            {
                'question': 'Can I schedule a callback?',
                'answer': 'Yes, you can schedule a callback through our website for your convenience.',
                'category': 'Support'
            },
            {
                'question': 'Do you offer support in other languages?',
                'answer': 'We currently offer support in English and Spanish.',
                'category': 'Support'
            },
            {
                'question': 'How quickly do you respond to emails?',
                'answer': 'We respond to all emails within 24 hours during business days.',
                'category': 'Support'
            },
            {
                'question': 'Can I speak to a manager?',
                'answer': 'You can request escalation to a supervisor through any of our support channels.',
                'category': 'Support'
            },
            {
                'question': 'Do you have a customer feedback program?',
                'answer': 'Yes, we welcome feedback through our website and email surveys.',
                'category': 'Support'
            },

            # Promotions & Loyalty (8 FAQs)
            {
                'question': 'Do you offer student discounts?',
                'answer': 'Yes, we offer 15% student discount with valid student ID verification.',
                'category': 'Promotions'
            },
            {
                'question': 'How does your loyalty program work?',
                'answer': 'Earn 1 point per dollar spent. 100 points = $10 reward. Tier benefits at 500 and 1000 points.',
                'category': 'Promotions'
            },
            {
                'question': 'Can I combine multiple coupon codes?',
                'answer': 'Only one coupon code can be used per order unless otherwise specified.',
                'category': 'Promotions'
            },
            {
                'question': 'Do you offer military discounts?',
                'answer': 'Yes, we offer 15% military discount for active duty and veterans with verification.',
                'category': 'Promotions'
            },
            {
                'question': 'How do I get your newsletter?',
                'answer': 'Subscribe to our newsletter in the website footer to receive exclusive offers and updates.',
                'category': 'Promotions'
            },
            {
                'question': 'Do you have a referral program?',
                'answer': 'Yes, refer friends and both you and your friend receive $10 off your next purchase.',
                'category': 'Promotions'
            },
            {
                'question': 'Are there birthday discounts?',
                'answer': 'Yes, join our loyalty program to receive a special birthday discount each year.',
                'category': 'Promotions'
            },
            {
                'question': 'Do you offer corporate discounts?',
                'answer': 'Yes, we offer corporate pricing for bulk orders. Contact our business sales team.',
                'category': 'Promotions'
            },

            # Technical & Website (7 FAQs)
            {
                'question': 'Is your website mobile friendly?',
                'answer': 'Yes, our website is fully responsive and optimized for all mobile devices.',
                'category': 'Technical'
            },
            {
                'question': 'What browsers do you support?',
                'answer': 'We support Chrome, Firefox, Safari, Edge, and other modern browsers.',
                'category': 'Technical'
            },
            {
                'question': 'How do I clear my shopping cart?',
                'answer': 'Remove individual items or click "Clear Cart" in your cart page to remove all items.',
                'category': 'Technical'
            },
            {
                'question': 'Can I save items for later?',
                'answer': 'Yes, click the heart icon to save items to your wishlist for future reference.',
                'category': 'Technical'
            },
            {
                'question': 'Do you have a mobile app?',
                'answer': 'Yes, our mobile app is available for download on iOS and Android devices.',
                'category': 'Technical'
            },
            {
                'question': 'How do I update my app?',
                'answer': 'App updates are available through the Apple App Store or Google Play Store.',
                'category': 'Technical'
            },
            {
                'question': 'What if the website is not working?',
                'answer': 'Clear your browser cache or try a different browser. If issues persist, contact technical support.',
                'category': 'Technical'
            }
        ]

        created_count = 0
        for faq_data in comprehensive_faqs:
            faq, created = FAQ.objects.get_or_create(
                question=faq_data['question'],
                defaults={
                    'answer': faq_data['answer'],
                    'category': faq_data['category']
                }
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'✅ Successfully loaded {created_count} comprehensive FAQs!')
        )
        self.stdout.write(
            self.style.SUCCESS(f'📊 Total FAQs in database: {FAQ.objects.count()}')
        )
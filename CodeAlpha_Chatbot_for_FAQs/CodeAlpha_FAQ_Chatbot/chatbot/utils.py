import numpy as np
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from .models import FAQ

print("🚀 Loading Enhanced FAQ Chatbot AI...")

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    print("✅ NLTK punkt tokenizer is available")
except LookupError:
    print("📥 Downloading NLTK punkt tokenizer...")
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
    print("✅ NLTK stopwords are available")
except LookupError:
    print("📥 Downloading NLTK stopwords...")
    nltk.download('stopwords')

class EnhancedFAQChatbot:
    def __init__(self):
        print("🤖 Initializing Enhanced FAQ Chatbot AI...")
        self.vectorizer = TfidfVectorizer(max_features=1000, stop_words='english', ngram_range=(1, 2))
        self.tfidf_matrix = None
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
        self.faqs = []
        self.is_trained = False
        print("✅ Enhanced FAQ Chatbot AI initialized")
        
    def preprocess_text(self, text):
        """Enhanced text preprocessing"""
        try:
            if not text or not isinstance(text, str):
                return ""
                
            # Convert to lowercase
            text = text.lower().strip()
            
            # Remove punctuation
            text = text.translate(str.maketrans('', '', string.punctuation))
            
            # Tokenize
            tokens = word_tokenize(text)
            
            # Remove stopwords and stem
            filtered_tokens = []
            for token in tokens:
                if token not in self.stop_words and token.isalpha() and len(token) > 2:
                    stemmed = self.stemmer.stem(token)
                    filtered_tokens.append(stemmed)
            
            return ' '.join(filtered_tokens)
            
        except Exception as e:
            print(f"❌ Error in text preprocessing: {e}")
            return ""
    
    def train(self):
        """Enhanced training for large datasets"""
        try:
            print("📚 Training AI with comprehensive FAQs...")
            self.faqs = list(FAQ.objects.filter(is_active=True))
            print(f"📖 Found {len(self.faqs)} FAQs for training")
            
            if not self.faqs:
                print("❌ No FAQs available for training")
                self.is_trained = False
                return False
                
            # Extract and preprocess questions
            questions = []
            valid_faqs = []
            
            for faq in self.faqs:
                processed_question = self.preprocess_text(faq.question)
                if processed_question.strip():
                    questions.append(processed_question)
                    valid_faqs.append(faq)
                else:
                    print(f"⚠️ Skipping FAQ with empty processed question: {faq.question}")
            
            if not questions:
                print("❌ No valid questions after preprocessing")
                self.is_trained = False
                return False
            
            self.faqs = valid_faqs  # Update with only valid FAQs
            print(f"🔧 Training on {len(questions)} valid processed questions")
            
            # Enhanced TF-IDF training
            self.tfidf_matrix = self.vectorizer.fit_transform(questions)
            self.is_trained = True
            
            # Show training statistics
            feature_names = self.vectorizer.get_feature_names_out()
            print(f"✅ AI training completed! Vocabulary size: {len(feature_names)}")
            print(f"📊 Training matrix shape: {self.tfidf_matrix.shape}")
            print("🎯 AI is now ready to answer questions!")
            return True
            
        except Exception as e:
            print(f"❌ Error during training: {e}")
            import traceback
            traceback.print_exc()
            self.is_trained = False
            return False
    
    def get_response(self, user_question, threshold=0.15):
        """Enhanced response generation with better matching"""
        try:
            print(f"\n🎯 Processing question: '{user_question}'")
            
            # Train if not trained
            if not self.is_trained:
                print("🔄 AI not trained, training now...")
                if not self.train():
                    return "I'm not trained yet. Please add some FAQs first.", 0.0
            
            if not self.faqs:
                return "No FAQs available. Please add some questions and answers first.", 0.0
            
            # Preprocess user question
            processed_question = self.preprocess_text(user_question)
            print(f"🔧 Processed question: '{processed_question}'")
            
            if not processed_question.strip():
                return "Please ask a clear question with meaningful words.", 0.0
            
            # Transform user question to TF-IDF vector
            user_vector = self.vectorizer.transform([processed_question])
            
            # Calculate cosine similarity with all FAQ questions
            similarities = cosine_similarity(user_vector, self.tfidf_matrix)
            
            # Get the best match
            best_match_idx = np.argmax(similarities)
            best_similarity = similarities[0, best_match_idx]
            
            print(f"📊 Best match index: {best_match_idx}, Similarity: {best_similarity:.4f}")
            
            # Get top 3 matches for better insights
            top_indices = np.argsort(similarities[0])[-3:][::-1]
            print("🔍 Top 3 matches:")
            for i, idx in enumerate(top_indices):
                print(f"  {i+1}. '{self.faqs[idx].question}' -> {similarities[0][idx]:.4f}")
            
            if best_similarity >= threshold:
                best_faq = self.faqs[best_match_idx]
                print(f"✅ Found strong match: '{best_faq.question}'")
                print(f"💡 Answer: '{best_faq.answer}'")
                return best_faq.answer, best_similarity
            else:
                print(f"❌ No good match found (threshold: {threshold}, best: {best_similarity:.4f})")
                
                # Provide helpful suggestions based on categories
                categories = set(faq.category for faq in self.faqs)
                category_list = ", ".join(sorted(categories))
                
                return f"I'm not sure about that specific question. The closest match had {best_similarity:.1%} relevance. Try asking about: {category_list}", best_similarity
                
        except Exception as e:
            print(f"❌ Error getting response: {e}")
            import traceback
            traceback.print_exc()
            return "Sorry, I encountered an error while processing your question.", 0.0

# Global enhanced chatbot instance
chatbot = EnhancedFAQChatbot()
print("🎉 Enhanced FAQ Chatbot AI is ready for comprehensive training!")
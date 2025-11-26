# CodeAlpha AI Internship Projects

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![AI](https://img.shields.io/badge/AI-NLP%2FML-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📂 Projects Overview

This repository contains two AI-powered applications developed during the CodeAlpha Artificial Intelligence Internship:

1. **🤖 AI-Powered FAQ Chatbot** - Intelligent question-answering system
2. **🌍 AI Translator** - Multilingual translation web application

---

# 🤖 AI-Powered FAQ Chatbot

## 🚀 Project Overview

This project is an **AI-powered FAQ Chatbot** built for the CodeAlpha Artificial Intelligence Internship. The chatbot uses Natural Language Processing (NLP) to understand user queries and return the most relevant answers from an FAQ database.

## ✨ Key Features

- 🤖 **AI Question Matching** using TF-IDF and cosine similarity  
- 📚 **80+ preloaded FAQs** across multiple categories  
- 🎯 **High accuracy** through advanced text preprocessing  
- 📊 **Confidence scoring** for responses  
- ⚡ **Real-time chat interface**  
- 🔧 **FAQ management dashboard**  
- 📱 **Responsive UI** for all devices  

## 🛠️ Technologies Used

- **Backend:** Django 4.2  
- **ML/NLP:** Scikit-learn, NLTK, NumPy  
- **Frontend:** HTML5, CSS, JavaScript, Bootstrap  
- **Database:** SQLite (dev), PostgreSQL ready  

## 🎯 AI Workflow

1. Text cleaning & tokenization  
2. Stop-word removal  
3. Stemming (Porter)  
4. TF-IDF vectorization  
5. Cosine similarity ranking  

## 🚀 Quick Start Guide

### 1. Clone the repo
```bash
git clone https://github.com/wonderrful003/CodeAlpha_Tasks.git
cd CodeAlpha_Tasks/Chatbot_for_FAQs
```

### 2. Create and activate virtual environment
```bash
python -m venv chatbot_env
source chatbot_env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Load sample FAQs
```bash
python manage.py load_comprehensive_faqs
```

### 6. Start the server
```bash
python manage.py runserver
```

### 7. Access the app
- **Chat Interface** → http://127.0.0.1:8000
- **FAQ Management** → http://127.0.0.1:8000/faqs
- **Admin Panel** → http://127.0.0.1:8000/admin

## 📁 Project Structure
```
Chatbot_for_FAQs/
├── chatbot/
├── faq_chatbot/
└── documentation/
```

## 🔧 API Endpoints
- `GET /` — Chat UI
- `POST /api/chat/` — Chatbot API
- `GET /faqs/` — FAQ manager
- `POST /faqs/` — Add FAQ

---

# 🌍 AI Translator - Multilingual Translation Web Application

A fast, AI-powered multilingual translation web application built with Django and Python. Supports 25+ languages including comprehensive African language support with Chichewa, Swahili, Yoruba, and more.

![Languages](https://img.shields.io/badge/Languages-25%2B-orange)
![African Languages](https://img.shields.io/badge/African%20Languages-15-yellow)

## 🚀 Features

- **🌐 25+ Languages** - Comprehensive global language support
- **🇿🇦 15 African Languages** - Specialized support for African languages including Chichewa, Swahili, Yoruba, Igbo, Hausa, and more
- **🤖 AI-Powered Translation** - Uses state-of-the-art MarianMT models from HuggingFace
- **⚡ Fast Performance** - Optimized with caching and lazy loading
- **🎨 Modern UI** - Clean black and white responsive design
- **📱 Real-time Translation** - Instant results with loading indicators and error handling
- **🔧 RESTful API** - Fully functional API for integration

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 4.2.7 + Django REST Framework
- **AI Models**: HuggingFace Transformers, PyTorch
- **Caching**: Django Cache Framework
- **Authentication**: Django CSRF Protection

### Frontend
- **UI Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.0
- **JavaScript**: Vanilla ES6+
- **Styling**: Custom CSS with glassmorphism effects

### AI/ML
- **Translation Models**: Helsinki-NLP MarianMT models
- **Inference**: PyTorch with GPU support (if available)
- **Tokenization**: SentencePiece, Sacremoses

## 🌐 Supported Languages

### European Languages
- English (`en`), Spanish (`es`), French (`fr`), German (`de`)
- Italian (`it`), Portuguese (`pt`), Russian (`ru`)

### Asian Languages
- Chinese (`zh`), Japanese (`ja`), Korean (`ko`), Arabic (`ar`)

### African Languages
- **Swahili** (`sw`) - East Africa
- **Yoruba** (`yo`) - West Africa
- **Igbo** (`ig`) - Nigeria
- **Hausa** (`ha`) - West Africa
- **Amharic** (`am`) - Ethiopia
- **Somali** (`so`) - Horn of Africa
- **Zulu** (`zu`) - South Africa
- **Xhosa** (`xh`) - South Africa
- **Kinyarwanda** (`rw`) - Rwanda
- **Chichewa** (`ny`) - Malawi, Zambia, Zimbabwe
- **Malagasy** (`mg`) - Madagascar
- **Lingala** (`ln`) - Central Africa
- **Shona** (`sn`) - Zimbabwe
- **Sesotho** (`st`) - Lesotho
- **Setswana** (`tn`) - Botswana

## 🚀 Quick Start Guide

### 1. Navigate to project
```bash
cd CodeAlpha_Tasks/Language_Translation_Tool
```

### 2. Create and activate virtual environment
```bash
python -m venv translator_env
source translator_env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
echo "SECRET_KEY=your-secret-key-here" > .env
echo "DEBUG=True" >> .env
```

### 5. Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start development server
```bash
python manage.py runserver
```

### 7. Access the application
Open http://127.0.0.1:8000/ in your browser

## 🔧 API Endpoints

- **POST** `/api/translate/` - Translate text
- **GET** `/api/languages/` - Get supported languages list
- **GET** `/api/health/` - Health check endpoint

### Example API Usage
```bash
curl -X POST http://127.0.0.1:8000/api/translate/ \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello, how are you?",
    "source_lang": "en",
    "target_lang": "ny"
  }'
```

## 📁 Project Structure
```
Language_Translation_Tool/
├── ai_translator/
├── translator/
├── services/
├── static/
└── templates/
```

---

## 🛠️ Installation for Both Projects

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/wonderrful003/CodeAlpha_Tasks.git
   cd CodeAlpha_Tasks
   ```

2. **Set up FAQ Chatbot**
   ```bash
   cd Chatbot_for_FAQs
   python -m venv chatbot_env
   source chatbot_env/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py load_comprehensive_faqs
   python manage.py runserver
   ```

3. **Set up AI Translator** (in new terminal)
   ```bash
   cd Language_Translation_Tool
   python -m venv translator_env
   source translator_env/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver 8001
   ```

## 🌐 Access Points

- **FAQ Chatbot**: http://127.0.0.1:8000
- **AI Translator**: http://127.0.0.1:8001

---

## 👥 Author

**Wonderful Ntepa**  
CodeAlpha AI Intern  
[LinkedIn](https://www.linkedin.com/in/wonderful-ntepa-52a07b229/) | [GitHub](https://github.com/wonderrful003)

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [HuggingFace](https://huggingface.co/) for state-of-the-art NLP models
- [Helsinki-NLP](https://github.com/Helsinki-NLP) for MarianMT translation models
- [Django Software Foundation](https://www.djangoproject.com/) for the web framework
- [CodeAlpha](https://www.codealpha.tech/) for the internship opportunity

---

⭐ **If you find these projects useful, consider starring the repository!**
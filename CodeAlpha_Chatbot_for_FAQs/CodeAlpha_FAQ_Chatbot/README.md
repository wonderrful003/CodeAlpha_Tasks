# AI-Powered FAQ Chatbot - CodeAlpha Internship Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![AI](https://img.shields.io/badge/AI-NLP%2FML-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

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
bash
git clone https://github.com/wonderrful003/CodeAlpha_FAQ_Chatbot.git
cd CodeAlpha_FAQ_Chatbot

2. Create and activate a virtual environment
python -m venv chatbot_env
source chatbot_env/bin/activate   # Windows: chatbot_env\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py migrate

5. Load sample FAQs
python manage.py load_comprehensive_faqs

6. Start the server
python manage.py runserver

7. Access the app

Chat Interface → http://127.0.0.1:8000

FAQ Management → http://127.0.0.1:8000/faqs

Admin Panel → http://127.0.0.1:8000/admin

📁 Project Structure
CodeAlpha_FAQ_Chatbot/
├── chatbot/
├── faq_chatbot/
└── documentation/

🔧 API Endpoints

GET / — Chat UI

POST /api/chat/ — Chatbot API

GET /faqs/ — FAQ manager

POST /faqs/ — Add FAQ

👥 Author

Wonderful Ntepa
CodeAlpha AI Intern
[LinkedIn](https://www.linkedin.com/in/wonderful-ntepa-52a07b229/) | [GitHub](https://github.com/wonderrful003)

⭐ If you find this project useful, consider starring the repository!

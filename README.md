# 📚 AI-Powered Study Buddy

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow)

## 📌 Project Overview
Students often struggle to digest complex concepts from lengthy lecture materials, and searching online frequently yields overwhelming or irrelevant results. 

The **AI-Powered Study Buddy** is a project designed to solve this by providing an instant, 24/7 learning aid. It leverages Natural Language Processing (NLP) to analyze dense study notes or PDF lecture slides, automatically generating simplified summaries and extracting core concepts for flashcards.

## ✨ Key Features
* **📄 PDF & Text Support:** Upload PDF lecture slides or paste raw text directly into the application.
* **🧠 AI Summarization:** Uses Hugging Face's sequence-to-sequence models to generate concise, abstractive summaries of long study materials.
* **💡 Flashcard Generator:** Automatically extracts core technical terms and keywords from the text to help build study flashcards.
* **⚡ Blazing Fast UI:** Built with Streamlit, featuring resource caching so the heavy AI models load efficiently.

## 🛠️ Technology Stack
* **Language:** Python
* **Frontend/UI:** Streamlit
* **Machine Learning:** Hugging Face Transformers, PyTorch
* **Document Processing:** PyPDF2

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/devidattamishra45/ai-study-buddy-capstone.git](https://github.com/devidattamishra45/ai-study-buddy-capstone.git)
   cd ai-study-buddy-capstone

2.Install the required dependencies:
 ```bash
pip install -r requirements.txt
3.Run the Streamlit application:
 ```bash
streamlit run app.py



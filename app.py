import streamlit as st
from transformers import pipeline
import PyPDF2
import re
from collections import Counter

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="AI Study Buddy", 
    page_icon="📚", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# HELPER FUNCTIONS (CACHED FOR PERFORMANCE)
# ==========================================
@st.cache_resource
def load_summarizer():
    """Loads the Hugging Face summarization pipeline."""
    # Using distilbart for a good balance of speed and performance
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def extract_text_from_pdf(file):
    """Extracts raw text from an uploaded PDF document."""
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

def generate_flashcard_keywords(text, num_keywords=10):
    """A lightweight NLP function to extract key terms for flashcards."""
    # Clean the text: remove non-alphanumeric characters and convert to lowercase
    clean_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    words = clean_text.split()
    
    # Filter out common English stop words to find actual key concepts
    stop_words = set([
        "the", "and", "is", "in", "to", "of", "it", "that", "this", "for", 
        "on", "with", "as", "by", "an", "be", "are", "from", "at", "or"
    ])
    meaningful_words = [word for word in words if word not in stop_words and len(word) > 4]
    
    # Get the most common words as our key concepts
    word_counts = Counter(meaningful_words)
    return [word[0] for word in word_counts.most_common(num_keywords)]

# ==========================================
# MAIN APPLICATION UI
# ==========================================
def main():
    # Sidebar styling and info
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3300/3300074.png", width=100)
        st.title("Settings & Info")
        st.write("Welcome to the AI-Powered Study Buddy! This tool helps students understand complex concepts by summarizing notes and extracting key flashcard terms.")
        st.markdown("---")
        st.write("**Developed by:** M NANTHINI")
        st.write("**Department:** CSE, ITER")
        
    # Main Header
    st.title("📚 AI-Powered Study Buddy Capstone")
    st.markdown("Upload your lecture slides (PDF) or paste your notes below. The AI will summarize the content into simple terms and generate core concept flashcards.")

    # Load AI Model
    summarizer = load_summarizer()

    # Input Method Selection
    input_method = st.radio("Choose your input method:", ("Paste Text", "Upload PDF"))
    
    study_text = ""

    # Handle Text Input
    if input_method == "Paste Text":
        study_text = st.text_area("Paste your study notes or lecture transcript here:", height=250)
        
    # Handle PDF Upload
    elif input_method == "Upload PDF":
        uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")
        if uploaded_file is not None:
            with st.spinner("Extracting text from PDF..."):
                study_text = extract_text_from_pdf(uploaded_file)
                st.success("PDF extracted successfully!")
                with st.expander("View Extracted Text"):
                    st.write(study_text[:1000] + "... (Text truncated for preview)")

    # Processing Button
    if st.button("Generate Study Materials", type="primary"):
        if len(study_text.split()) < 50:
            st.warning("Please provide at least 50 words of text for the AI to generate a meaningful summary.")
        else:
            st.markdown("---")
            
            # Create two columns for the output
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.subheader("📝 Simplified Summary")
                with st.spinner("AI is analyzing and summarizing your notes..."):
                    # Calculate dynamic max length based on input size
                    input_length = len(study_text.split())
                    max_len = min(150, int(input_length * 0.5))
                    
                    try:
                        # Chunk the text to prevent token limits (handling first 1024 tokens simply)
                        truncated_text = " ".join(study_text.split()[:800])
                        summary = summarizer(truncated_text, max_length=max_len, min_length=30, do_sample=False)
                        st.info(summary[0]['summary_text'])
                    except Exception as e:
                        st.error(f"An error occurred during summarization: {e}")

            with col2:
                st.subheader("💡 Key Flashcard Terms")
                with st.spinner("Extracting core concepts..."):
                    keywords = generate_flashcard_keywords(study_text)
                    for i, word in enumerate(keywords):
                        st.markdown(f"**{i+1}. {word.capitalize()}**")
                        
            st.success("Study materials generated successfully! Good luck with your preparation.")

if __name__ == "__main__":
    main()
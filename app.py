import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="Fake News Detection", layout="wide")

st.title("📰 Fake News Detection System")

# Sidebar navigation
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Select a page:", ["Detection", "About"])

if page == "About":
    st.markdown("""
    # About This Project
    
    **Author:** Mannuru Lucky Balaji (2300030405)
    
    ## Project Overview
    The Fake News Detection System is a Machine Learning-based web application developed to automatically identify whether a news article is real or fake. With the rapid growth of digital media platforms and social networks, misinformation spreads quickly, causing confusion and societal harm.
    
    ## System Architecture
    - **Frontend:** Streamlit interface for text input and predictions
    - **Backend:** Scikit-learn ML models for classification
    - **Algorithm:** TF-IDF Vectorizer + Logistic Regression
    - **Datasets:** Trained on real and fake news datasets
    
    ## Technical Stack
    - TF-IDF Vectorization for text feature extraction
    - Logistic Regression for binary classification
    - Pandas for data processing
    - Streamlit for interactive UI
    
    ## Key Features
    1. Real-time news verification
    2. Simple, interactive interface
    3. Fast predictions using ML models
    4. Supports multiple text inputs
    
    ## Future Enhancements
    - Integration with deep learning models (LSTM, BERT)
    - Multi-language support
    - Real-time news API integration
    - Confidence scoring and explainability
    
    """)
    st.stop()

# Detection page
st.header("Check Your News Here")

import os

# Load both datasets
base_dir = os.path.dirname(os.path.abspath(__file__))
fake = pd.read_csv(os.path.join(base_dir, "Fake.csv"))
true = pd.read_csv(os.path.join(base_dir, "True.csv"))

fake["label"] = "FAKE"
true["label"] = "REAL"

df = pd.concat([fake, true])

X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer(stop_words="english")
X_vectorized = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vectorized, y)

news_input = st.text_area("Enter news text:")

if st.button("Check News"):
    input_vector = vectorizer.transform([news_input])
    prediction = model.predict(input_vector)

    if prediction[0] == "FAKE":
        st.error("⚠️ This News is FAKE")
    else:
        st.success("✅ This News is REAL")

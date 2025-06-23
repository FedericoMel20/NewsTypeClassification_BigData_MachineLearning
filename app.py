# streamlit_app.py

import streamlit as st
import joblib
import re

# Load saved model, vectorizer, and encoder
model = joblib.load('news_classifier_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Function to clean input text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Streamlit UI
st.set_page_config(page_title="News Type Classifier", layout="centered")
st.title("📰 News Headline Category Classifier")
st.write("Enter a news headline below to predict its category.")

# Input field
user_input = st.text_area("📝 News Headline", "")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a headline.")
    else:
        # Preprocess input
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])

        # Predict
        pred_label = model.predict(vectorized)[0]
        pred_class = label_encoder.inverse_transform([pred_label])[0]

        # Output result
        st.success(f"🧠 Predicted Category: **{pred_class}**")

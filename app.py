import streamlit as st
from textblob import TextBlob

# Page configuration
st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="📊", layout="centered")

# App Header
st.title("AI Sentiment Analysis Dashboard")
st.header("By Muhannad Alasmari")
st.write("A machine learning-powered web app to analyze the emotional tone of customer reviews, feedback, or text.")

# User Input Section
st.subheader("Enter Text for Analysis")
user_text = st.text_area("Type or paste your review here:", "I absolutely love this product! The quality exceeded my expectations.")

# Analysis Button
if st.button("Analyze Sentiment"):
    if user_text.strip():
        # Perform NLP Sentiment Analysis
        blob = TextBlob(user_text)
        polarity = blob.sentiment.polarity  # Range: -1.0 (Negative) to 1.0 (Positive)
        
        # Display Results
        st.divider()
        st.subheader("Results")
        
        if polarity > 0.1:
            st.success(f"**Positive Sentiment** 😊 (Polarity Score: {polarity:.2f})")
        elif polarity < -0.1:
            st.error(f"**Negative Sentiment** 😞 (Polarity Score: {polarity:.2f})")
        else:
            st.info(f"**Neutral Sentiment** 😐 (Polarity Score: {polarity:.2f})")
    else:
        st.warning("Please enter some text before analyzing.")

# Footer note
st.markdown("---")
st.markdown("Built with Python & Streamlit | ML Web App")

import streamlit as st
from textblob import TextBlob

# Page configuration
st.set_page_config(page_title="AI Sentiment & Action Hub", page_icon="📊", layout="centered")

# App Header
st.title("AI Sentiment Analysis & Action Hub")
st.write("A machine learning web app that analyzes customer feedback and generates automated business action plans.")

# User Input Section
st.subheader("Enter Text for Analysis")
user_text = st.text_area("Type or paste your review here:", "I absolutely love this product! The quality exceeded my expectations.")

# Analysis Button
if st.button("Analyze & Generate Action Plan"):
    if user_text.strip():
        # Phase 1: Sentiment Analysis
        blob = TextBlob(user_text)
        polarity = blob.sentiment.polarity  # Range: -1.0 (Negative) to 1.0 (Positive)
        
        # Display Sentiment Results
        st.divider()
        st.subheader("Phase 1: Sentiment Insights")
        
        if polarity > 0.1:
            st.success(f"**Positive Sentiment** 😊 (Polarity Score: {polarity:.2f})")
        elif polarity < -0.1:
            st.error(f"**Negative Sentiment** 😞 (Polarity Score: {polarity:.2f})")
        else:
            st.info(f"**Neutral Sentiment** 😐 (Polarity Score: {polarity:.2f})")
            
        # Phase 2: Actionable Recommendations Generator
        st.subheader("Phase 2: Recommended Business Actions")
        
        if polarity > 0.1:
            st.markdown("""
            * **Marketing Action:** Flag this review to be highlighted as a user testimonial on social media or the landing page.
            * **Customer Success:** Send an automated loyalty reward or thank-you note to deepen customer retention.
            * **Product Team:** Log this as validated positive feedback for the current feature set.
            """)
        elif polarity < -0.1:
            st.markdown("""
            * **Urgent Support:** Route this review immediately to the customer support ticket queue for high-priority resolution.
            * **Quality Assurance:** Flag the mentioned product or service area for an internal bug or quality check.
            * **Follow-up:** Send a personalized apology email offering a refund or a replacement to win back trust.
            """)
        else:
            st.markdown("""
            * **Customer Engagement:** Send a gentle follow-up survey asking what could be improved to turn their neutral experience into a positive one.
            * **Product Insight:** Analyze keywords in this review to identify missing features or unclear documentation.
            """)
            
    else:
        st.warning("Please enter some text before analyzing.")

# Footer note
st.markdown("---")
st.markdown("Built with Python & Streamlit | ML Web App")

import os
import joblib
import streamlit as st
import time

# Load model and vectorizer
model = joblib.load(os.path.join("models", "logistic_model.pkl"))
vectorizer = joblib.load(os.path.join("models", "tfidf_vectorizer.pkl"))

# Page setup
st.set_page_config(page_title="Scam Detector", page_icon="🔍")
st.title("🔍 Scam Message Detector")
st.markdown("Detect whether a message is a scam using a machine learning model.")

# Cooldown mechanism (basic rate limit)
COOLDOWN_SECONDS = 5
if "last_submit_time" not in st.session_state:
    st.session_state.last_submit_time = 0

# Input
user_input = st.text_area("Paste the message you received:", height=150)

# Button + Logic
if st.button("Analyze"):
    now = time.time()
    if now - st.session_state.last_submit_time < COOLDOWN_SECONDS:
        remaining = int(COOLDOWN_SECONDS - (now - st.session_state.last_submit_time))
        st.warning(f"⏳ Please wait {remaining} more seconds before submitting again.")
    elif not user_input.strip():
        st.warning("⚠️ Please enter a message to analyze.")
    else:
        st.session_state.last_submit_time = now
        with st.spinner("Analyzing message..."):
            vectorized_input = vectorizer.transform([user_input])
            prediction = model.predict(vectorized_input)[0]
            if prediction == "scam":
                st.error("🚨 This message appears to be **a scam**.")
            else:
                st.success("✅ This message appears to be **not a scam**.")

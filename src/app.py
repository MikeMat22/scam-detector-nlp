import streamlit as st
from joblib import load
import os
from streamlit_limiter import RateLimiter
import concurrent.futures
from PIL import Image

# Rate limit: 5 requests per minute per IP
RateLimiter(limit=5, period=60)

# Load model and vectorizer
MODEL_PATH = "models/logistic_model.pkl"
VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"

model = load(MODEL_PATH)
vectorizer = load(VECTORIZER_PATH)

# Timeout prediction wrapper
def predict_with_timeout(predict_fn, args, timeout=5):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(predict_fn, *args)
        try:
            return future.result(timeout=timeout)
        except concurrent.futures.TimeoutError:
            return "⚠️ Prediction timeout exceeded!"

# Prediction function
def predict(text):
    vec_text = vectorizer.transform([text])
    return model.predict(vec_text)[0]

# UI setup
st.set_page_config(page_title="Scam Detector", page_icon="🕵️")

# Load and display logo
logo_path = "static/logo.png"
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=80)

st.title("🕵️ Scam Detector")
st.write("Enter a message below to check if it's suspicious.")

# User input
user_input = st.text_area("📩 Message", height=150)

if st.button("🔍 Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a message to check.")
    else:
        with st.spinner("Analyzing..."):
            result = predict_with_timeout(predict, [user_input], timeout=5)

        if result == "scam":
            st.error("⚠️ This message is likely a scam!")
        elif result == "not-scam":
            st.success("✅ This message appears to be safe.")
        else:
            st.warning(str(result))

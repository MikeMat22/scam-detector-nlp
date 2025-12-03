import streamlit as st
import joblib
import re

# Load model and vectorizer
model = joblib.load("models/logistic_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Basic cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

# Streamlit app layout
st.set_page_config(page_title="Scam Message Detector")
st.title("💬 Scam Message Detector")

st.write("Enter a message below to check if it's a potential scam:")

user_input = st.text_area("Message:", "")

if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        cleaned = clean_text(user_input)
        vect_text = vectorizer.transform([cleaned])
        prediction = model.predict(vect_text)[0]

        if prediction == "scam":
            st.error("🚨 This message is likely a SCAM.")
        else:
            st.success("✅ This message looks safe.")

st.markdown("---")
st.caption("Built by Michal · Logistic Regression · scikit-learn · Streamlit")

import joblib
import re

# Load the trained model and vectorizer
model = joblib.load("models/logistic_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Get user input
message = input("Enter a message to classify (scam or not): ")

# Preprocess the message (same logic as in train.py)
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

cleaned_message = clean_text(message)

# Transform and predict
vectorized = vectorizer.transform([cleaned_message])
prediction = model.predict(vectorized)[0]

# Output result
print(f"Prediction: {'SCAM' if prediction == 'scam' else 'NOT SCAM'}")

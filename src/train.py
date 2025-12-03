import os
import pandas as pd
import joblib
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Data loading
df = pd.read_csv("data/messages.csv")

# Text cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

df['message'] = df['message'].apply(clean_text)

# Vector
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['message'])
y = df['label']

# Split training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training model
model = LogisticRegression()
model.fit(X_train, y_train)

# Valuation
y_pred = model.predict(X_test)
print("📊 Classification result:\n")
print(classification_report(y_test, y_pred))

# Save model + vector
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/logistic_model.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("\n✅ Model is successfully saved in /models/")

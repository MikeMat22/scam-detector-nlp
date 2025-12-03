import pandas as pd
import joblib
import re
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("data/messages.csv")

# Basic text cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

df["message"] = df["message"].apply(clean_text)

# Prepare data
X = df["message"]
y = df["label"]

# Load vectorizer and model
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
model = joblib.load("models/logistic_model.pkl")

# Transform features
X_vect = vectorizer.transform(X)

# Split data for evaluation
_, X_test, _, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

# Make predictions
y_pred = model.predict(X_test)

# Print classification report
print("📊 Classification Report:\n")
print(classification_report(y_test, y_pred))

# Plot confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=["scam", "not-scam"])
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", xticklabels=["Scam", "Not Scam"], yticklabels=["Scam", "Not Scam"])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("models/confusion_matrix.png")
print("\n✅ Confusion matrix saved to models/confusion_matrix.png")

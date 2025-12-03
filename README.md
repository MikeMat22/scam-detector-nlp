# 🛡️ AI Scam Message Detector (NLP + scikit-learn)

This project uses Natural Language Processing to classify short messages as **scam** or **legit** using classic machine learning techniques.

## 🔍 About

Scam messages and phishing attacks are a growing problem in emails, SMS, and social platforms.  
This AI tool analyzes text messages and predicts whether the message is likely a scam.

## 🧠 Tech Stack

- Python 3
- scikit-learn (Logistic Regression)
- pandas
- TfidfVectorizer for text preprocessing
- Dataset: Custom collection of scam vs. non-scam messages

## 🗂️ Project Structure

scam-detector-nlp/
├── data/
│   └── messages.csv
├── src/
│   ├── train.py
│   └── evaluate.py
├── README.md
└── requirements.txt

## 📈 Future Ideas

- Deploy as an API
- Build web frontend (e.g. Streamlit or Flask)
- Train more advanced models (e.g. LSTM, Transformers)

## 📬 Author

[Michal Matějček](https://www.linkedin.com/in/michal-matejcek/)

# 🕵🏻‍♂️ Scam Detector NLP

A simple Natural Language Processing (NLP) project to detect scam messages using machine learning (scikit-learn).

## 🔧 Project Structure

```
scam-detector-nlp/
├── data/
│   └── messages.csv            # Training dataset
├── models/
│   ├── logistic_model.pkl      # Trained Logistic Regression model
│   └── tfidf_vectorizer.pkl    # Trained TF-IDF vectorizer
├── src/
│   ├── train.py                # Script to train the model
│   └── evaluate.py             # Script to evaluate the model on custom input
├── app.py                      # Streamlit web interface
├── static/
│   └── logo.png                # Optional logo for the UI
├── requirements.txt           # Required Python packages
└── README.md                  # Project documentation
```

## 🧪 How to Use Locally

1. Clone the repository:
```bash
git clone https://github.com/MikeMat22/scam-detector-nlp.git
cd scam-detector-nlp
```

2. Create and activate a virtual environment (recommended):
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Train the model:
```bash
python src/train.py
```

5. Run the app:
```bash
streamlit run app.py
```

## 🚀 Live Demo

Try the deployed version here:
👉 (https://scam-detector-nlp.onrender.com)

## 📂 Dataset
The training data is in `data/messages.csv` with the format:
```
message,label
"Your package has been held...",scam
"Hey, just checking in...",not-scam
```

## 👨‍💻 Author
LinkedIn: [Michal Matejcek](https://www.linkedin.com/in/michal-matejcek/)

---

✅ Built with scikit-learn + Streamlit
💡 Educational project by an aspiring AI Engineer

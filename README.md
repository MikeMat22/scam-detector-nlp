# AI Scam Message Detector (NLP + scikit-learn)

This project uses Natural Language Processing to classify short messages as **scam** or **legit** using classic machine learning techniques.

Live demo: [https://scam-detector-nlp.onrender.com](https://scam-detector-nlp.onrender.com)


## About

Scam messages and phishing attacks are a growing problem in emails, SMS, and social platforms.  
This AI tool analyzes text messages and predicts whether the message is likely a scam.

## Tech Stack

- **Python 3.11**
- **scikit-learn** – model training
- **Streamlit** – frontend + backend app
- **TF-IDF vectorizer** – text processing
- **Pandas + Regex** – data cleaning and manipulation
- **Joblib** – model saving/loading
- **Render** – cloud deployment

## Project Structure

```  
scam-detector-nlp/
├── assets/            # Logo, images, optional screenshot
├── data/              # Raw and processed datasets (if used)
├── models/            # Saved ML model + vectorizer (logistic_model.pkl, tfidf_vectorizer.pkl)
├── src/
│   ├── app.py         # Streamlit application
│   ├── train.py       # Script to train the ML model
│   └── fix_dataset.py # (Optional) Data cleaning / preprocessing script
├── requirements.txt   # Python dependencies
├── .gitignore         # excludes .venv, compiled files etc.
└── README.md          # This file
```  

## Future Ideas

- Deploy as an API
- Build web frontend (e.g. Streamlit or Flask)
- Train more advanced models (e.g. LSTM, Transformers)

## Sample Results
Accuracy:    96%
Precision:   99%
Recall:      71%
F1-score:    83%

## How to Run Locally
```
1. Clone the repository:

git clone https://github.com/MikeMat22/scam-detector-nlp.git
cd scam-detector-nlp

2.	Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4.	Launch the app:

python -m streamlit run src/app.py
``` 

## Author

[Michal Matějček](https://www.linkedin.com/in/michal-matejcek/)
AI Engineer · Made in Czech Republic

Disclaimer

This application is for educational and informational purposes only. It provides automated predictions based on a trained ML model and should not be considered a guaranteed scam detection service.

from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
import joblib
import re

app = FastAPI()

# Template folder
templates = Jinja2Templates(directory="../templates")

# Load trained model and vectorizer
model = joblib.load("../model/model.pkl")
vectorizer = joblib.load("../model/vectorizer.pkl")

# Suspicious keywords list
suspicious_words = [
    "win", "winner", "lottery", "urgent", "free",
    "claim", "prize", "bank", "otp", "click",
    "offer", "suspended", "update", "verify",
    "reward", "blocked", "alert"
]

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": None,
        "confidence": None,
        "risk": None,
        "highlighted_message": None
    })

@app.post("/predict", response_class=HTMLResponse)
def predict(request: Request, message: str = Form(...)):

    # Convert text to vector
    vector = vectorizer.transform([message])

    # Prediction
    prediction = model.predict(vector)[0]
    probability = model.predict_proba(vector)[0][1]  # Spam probability
    confidence = round(probability * 100, 2)

    # Risk Level Logic (Improved)
    if confidence < 50:
        risk = "Low Risk 🟢"
    elif confidence < 80:
        risk = "Medium Risk 🟡"
    else:
        risk = "High Risk 🔴"

    result = "Spam Message 🚨" if prediction == 1 else "Safe Message ✅"

    # Highlight suspicious words
    highlighted_message = message
    for word in suspicious_words:
        pattern = re.compile(rf"\b({word})\b", re.IGNORECASE)
        highlighted_message = pattern.sub(
            r"<span style='color:red;font-weight:bold;'>\1</span>",
            highlighted_message
        )

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "confidence": confidence,
        "risk": risk,
        "highlighted_message": highlighted_message
    })
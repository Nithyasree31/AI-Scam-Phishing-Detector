 🔐 AI Scam & Phishing Message Detector

An AI-powered web application that detects scam and phishing messages using Natural Language Processing (NLP) and Machine Learning.

Built for hackathon submission.

---

🚀 Project Overview

Digital scam messages are increasing rapidly, especially SMS phishing and OTP fraud.  

This project provides a simple web interface where users can paste a suspicious message and instantly receive:

- Spam / Safe classification
- Scam probability percentage
- Risk level (Low / Medium / High)
- Suspicious word highlighting

The goal is to improve awareness and prevent digital fraud.

---

 🧠 Machine Learning Approach

Model Pipeline:

Text Input  
→ TF-IDF Vectorization  
→ Logistic Regression Classifier  
→ Probability-Based Risk Scoring  

Why Logistic Regression?

- Lightweight and fast
- Performs well for short text classification
- Provides probability output for explainability

---

 🎯 Features

✔ Spam / Safe Detection  
✔ Probability Score Output  
✔ Risk Level Classification  
✔ Suspicious Word Highlighting  
✔ Clean Web UI  
✔ FastAPI Backend  

---

🛠 Tech Stack

- Python
- FastAPI
- Scikit-learn
- HTML / CSS
- Uvicorn

---

---

▶ How to Run the Project

1. Install dependencies:

pip install -r backend/requirements.txt

2. Train the model:

cd backend
python train.py

3. Run the server:

uvicorn app:app --reload

4. Open in browser:

http://127.0.0.1:8000
---

 🎬 Example Output

Input:
"URGENT! Your bank account will be suspended. Click here to update KYC."

Output:
- Scam Probability: High
- Risk Level: High Risk
- Suspicious words highlighted in red
- ---

👩‍💻 Team Members

| Nithyasree S - Machine Learning Model & Backend Development |
| Nithya sree S - Frontend Development |
| Priya Dharshini H - UI/UX Design |
| Pavithra V - Testing & Documentation |

Hackathon Project – AI Scam & Phishing Detection

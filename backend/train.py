import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Load dataset
data = pd.read_csv("../dataset/spam.csv", sep='\t', header=None, names=['label','message'])

# Convert labels
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['message'])
y = data['label']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
os.makedirs("../model", exist_ok=True)
joblib.dump(model, "../model/model.pkl")
joblib.dump(vectorizer, "../model/vectorizer.pkl")

print("Model trained and saved successfully!")
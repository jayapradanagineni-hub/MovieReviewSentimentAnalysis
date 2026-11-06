import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

data = {
    "review": [
        "This movie is absolutely fantastic",
        "Amazing movie with excellent acting",
        "I really loved this movie",
        "Wonderful story and beautiful direction",
        "Best movie I have ever watched",
        "The movie was very entertaining",
        "Excellent performance by the actors",
        "A masterpiece with great music",
        "I enjoyed every minute of this film",
        "Superb movie with a brilliant story",
        "This movie is very boring",
        "Worst movie I have ever seen",
        "Terrible acting and poor direction",
        "I hated this movie completely",
        "Very disappointing film",
        "The story was boring and confusing",
        "Waste of time and money",
        "Bad movie with horrible acting",
        "I regret watching this film",
        "Awful movie with no entertainment"
    ],
    "sentiment": [
        "Positive", "Positive", "Positive", "Positive", "Positive",
        "Positive", "Positive", "Positive", "Positive", "Positive",
        "Negative", "Negative", "Negative", "Negative", "Negative",
        "Negative", "Negative", "Negative", "Negative", "Negative"
    ]
}

df = pd.DataFrame(data)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

model.fit(df["review"], df["sentiment"])

joblib.dump(model, "sentiment_model.pkl")

print("Model trained successfully!")
print("Model saved as sentiment_model.pkl")
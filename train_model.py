
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# 1. Load the dataset
data_path = Path("data") / "support_tickets.csv"
df = pd.read_csv(data_path)

X = df["ticket_text"].astype(str)

# Create the folder for trained models
model_dir = Path("models")
model_dir.mkdir(exist_ok=True)

# 2. Train and evaluate one model for each prediction task
targets = ["category", "priority"]

for target in targets:
    print("\n" + "=" * 50)
    print(f"Training {target.upper()} classifier")
    print("=" * 50)

    y = df[target].astype(str)

    # Hold out 25% of the examples for evaluation
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    # Convert words into numerical features, then classify
    model = Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                lowercase=True,
                ngram_range=(1, 2)
            )
        ),
        (
            "classifier",
            LogisticRegression(max_iter=1000)
        )
    ])

    # Train on the training portion
    model.fit(X_train, y_train)

    # Evaluate on examples not used in this training run
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    print(f"Test examples: {len(y_test)}")
    print(f"Accuracy: {accuracy:.2%}")

    print("\nClassification report:")
    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )

    # Train the final saved model on all available examples
    model.fit(X, y)

    model_path = model_dir / f"{target}_classifier.pkl"
    joblib.dump(model, model_path)

    print(f"Saved model: {model_path}")

print("\nBoth classifiers have been trained and saved!")

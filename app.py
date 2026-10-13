
from pathlib import Path

import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

# Find the trained models inside this project.
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

category_model = joblib.load(
    MODEL_DIR / "category_classifier.pkl"
)

priority_model = joblib.load(
    MODEL_DIR / "priority_classifier.pkl"
)


@app.route("/", methods=["GET", "POST"])
def home():
    ticket = ""
    category = None
    priority = None
    error = None

    if request.method == "POST":
        ticket = request.form.get("ticket", "").strip()

        if not ticket:
            error = "Please enter a customer support message."
        else:
            category = category_model.predict([ticket])[0]
            priority = priority_model.predict([ticket])[0]

    return render_template(
        "index.html",
        ticket=ticket,
        category=category,
        priority=priority,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)

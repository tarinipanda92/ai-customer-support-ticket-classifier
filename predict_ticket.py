import joblib
from pathlib import Path

category_model = joblib.load(
    Path("models") / "category_classifier.pkl"
)

priority_model = joblib.load(
    Path("models") / "priority_classifier.pkl"
)

print("=" * 45)
print("AI CUSTOMER SUPPORT TICKET CLASSIFIER")
print("Type 'exit' to close.")
print("=" * 45)

while True:
    ticket = input("\nEnter customer message: ").strip()

    if ticket.lower() == "exit":
        print("Classifier closed.")
        break

    if not ticket:
        print("Please enter a message.")
        continue

    category = category_model.predict([ticket])[0]
    priority = priority_model.predict([ticket])[0]

    print("\n--- Prediction Results ---")
    print("Category:", category)
    print("Priority:", priority)
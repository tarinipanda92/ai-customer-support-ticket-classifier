
import pandas as pd
from pathlib import Path

tickets = [
    # Billing
    ("I was charged twice for my subscription.", "Billing", "High"),
    ("There is an unexpected charge on my account.", "Billing", "High"),
    ("My payment was deducted but my order failed.", "Billing", "High"),
    ("Please investigate a duplicate payment.", "Billing", "High"),
    ("I need a refund for an incorrect charge.", "Billing", "Medium"),
    ("My refund has not arrived yet.", "Billing", "Medium"),
    ("My credit card payment keeps failing.", "Billing", "Medium"),
    ("The invoice total seems incorrect.", "Billing", "Medium"),
    ("I cannot update my billing information.", "Billing", "Medium"),
    ("My subscription renewal payment failed.", "Billing", "Medium"),
    ("Please explain the latest invoice.", "Billing", "Low"),
    ("Can you send me a copy of my receipt?", "Billing", "Low"),
    ("Where can I download my monthly invoice?", "Billing", "Low"),
    ("I want to know my subscription price.", "Billing", "Low"),
    ("How do I change my payment method?", "Billing", "Low"),
    ("Please explain the taxes on my bill.", "Billing", "Low"),

    # Technical Support
    ("The application is completely down.", "Technical Support", "High"),
    ("I cannot access the service because it keeps crashing.", "Technical Support", "High"),
    ("The website is unavailable for all my work.", "Technical Support", "High"),
    ("My system stopped working after the update.", "Technical Support", "High"),
    ("The app crashes every time I open it.", "Technical Support", "High"),
    ("I am getting an error when saving important work.", "Technical Support", "High"),
    ("The application is running very slowly.", "Technical Support", "Medium"),
    ("A feature stopped working this morning.", "Technical Support", "Medium"),
    ("I receive an error when uploading a file.", "Technical Support", "Medium"),
    ("The dashboard is not displaying the correct data.", "Technical Support", "Medium"),
    ("My notifications are not working.", "Technical Support", "Medium"),
    ("The search function returns no results.", "Technical Support", "Medium"),
    ("How can I change the display settings?", "Technical Support", "Low"),
    ("Where can I find the user guide?", "Technical Support", "Low"),
    ("How do I export a report?", "Technical Support", "Low"),
    ("Please explain how to use the search feature.", "Technical Support", "Low"),

    # Account Access
    ("I am locked out of my account.", "Account Access", "High"),
    ("Someone may have accessed my account without permission.", "Account Access", "High"),
    ("My account was compromised and I cannot sign in.", "Account Access", "High"),
    ("I cannot access my account before an important deadline.", "Account Access", "High"),
    ("My password reset link does not work.", "Account Access", "Medium"),
    ("The verification code is not arriving.", "Account Access", "Medium"),
    ("My account login keeps failing.", "Account Access", "Medium"),
    ("I cannot complete two-factor authentication.", "Account Access", "Medium"),
    ("My account is showing an unexpected sign-in error.", "Account Access", "Medium"),
    ("The email verification process failed.", "Account Access", "Medium"),
    ("How can I change my account email address?", "Account Access", "Low"),
    ("I forgot where to update my profile.", "Account Access", "Low"),
    ("How do I change my password?", "Account Access", "Low"),
    ("Please help me update my profile picture.", "Account Access", "Low"),
    ("Where can I manage my account preferences?", "Account Access", "Low"),
    ("How do I enable two-factor authentication?", "Account Access", "Low"),

    # Shipping
    ("My package is missing and the delivery says completed.", "Shipping", "High"),
    ("My urgent package has not arrived.", "Shipping", "High"),
    ("The tracking says delivered but I did not receive it.", "Shipping", "High"),
    ("My shipment appears to be lost.", "Shipping", "High"),
    ("My package contains the wrong item and I need urgent help.", "Shipping", "High"),
    ("My shipment has been delayed for several days.", "Shipping", "Medium"),
    ("The tracking information has not updated.", "Shipping", "Medium"),
    ("My package is stuck at the sorting facility.", "Shipping", "Medium"),
    ("The delivery date has changed unexpectedly.", "Shipping", "Medium"),
    ("I received only part of my order.", "Shipping", "Medium"),
    ("How do I track my package?", "Shipping", "Low"),
    ("Can I update my delivery address?", "Shipping", "Low"),
    ("What are the standard delivery times?", "Shipping", "Low"),
    ("Can you tell me which courier handles my order?", "Shipping", "Low"),
    ("How can I request a delivery time change?", "Shipping", "Low"),
    ("Where can I find my tracking number?", "Shipping", "Low"),
]

df = pd.DataFrame(
    tickets,
    columns=["ticket_text", "category", "priority"]
)

output_folder = Path("data")
output_folder.mkdir(exist_ok=True)

output_file = output_folder / "support_tickets.csv"
df.to_csv(output_file, index=False)

print("Dataset created successfully!")
print("File:", output_file)
print("Total tickets:", len(df))

print("\nTickets by category:")
print(df["category"].value_counts().to_string())

print("\nTickets by priority:")
print(df["priority"].value_counts().to_string())

print("\nFirst five rows:")
print(df.head().to_string(index=False))

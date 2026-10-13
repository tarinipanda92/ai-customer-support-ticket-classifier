

\# AI Customer Support Ticket Classifier



A machine learning web application that classifies customer support messages by category and estimates their priority using Python, Scikit-learn, and Flask.



\## Features



\- Classifies tickets into Billing, Technical Support, Account Access, and Shipping.

\- Predicts ticket priority as High, Medium, or Low.

\- Uses TF-IDF text features and Logistic Regression.

\- Provides an interactive web interface built with Flask, HTML, and CSS.

\- Saves trained models for reuse.



\## Technology Stack



\- Python

\- Pandas

\- Scikit-learn

\- TF-IDF

\- Logistic Regression

\- Flask

\- HTML and CSS

\- Joblib

\- Git and GitHub



\## Project Structure



```text

AI-Customer-Support-Classifier/

├── app.py

├── create\_dataset.py

├── train\_model.py

├── predict\_ticket.py

├── requirements.txt

├── data/

│   └── support\_tickets.csv

├── models/

│   ├── category\_classifier.pkl

│   └── priority\_classifier.pkl

├── templates/

│   └── index.html

└── static/

&#x20;   └── style.css

```



\## Setup and Installation



\### 1. Clone the repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd AI-Customer-Support-Classifier

```



\### 2. Create and activate the environment



```bash

conda create -n support-ticket-ai python=3.11 -y

conda activate support-ticket-ai

```



\### 3. Install dependencies



```bash

python -m pip install -r requirements.txt

```



\### 4. Start the web application



```bash

python app.py

```



Open http://127.0.0.1:5000 in your browser.



If the trained model files are unavailable, generate the dataset and train the models first:



```bash

python create\_dataset.py

python train\_model.py

```



\## Current Evaluation



Initial evaluation on a held-out sample of 16 tickets per task:



\- Category classification accuracy: 62.5%

\- Priority classification accuracy: 50.0%



These are preliminary results from a small, manually created dataset. They do not establish production-level reliability.



\## Limitations and Future Improvements



\- Expand the dataset with more diverse and representative examples.

\- Improve performance through cross-validation and better evaluation.

\- Review priority predictions before acting on them.

\- Add confidence indicators, ticket history, and a dashboard.

\- Deploy the application online after further testing.



\## Disclaimer



This is an educational machine learning project. Predictions should be reviewed by a human before being used to make real customer-support decisions.




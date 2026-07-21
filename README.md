Start Services: Run docker compose up -d in terminal.

Setup Env: Run make setup.

Execute Pipeline: Run python src/train.py.

Open MLflow UI: Navigate to http://localhost:5000 in your browser.

    You will see the Fraud_Detection_Bakeoff experiment.

    Select runs to open the MLflow Compare View (Day 036).

    Check the Models tab to see FraudClassifier version 1 (Days 025 & 030).

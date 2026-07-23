Start Services: Run docker compose up -d in terminal.

Setup Env: Run make setup.

Execute Pipeline: Run python src/train.py.

Open MLflow UI: Navigate to http://localhost:5000 in your browser.

    You will see the Fraud_Detection_Bakeoff experiment.

    Select runs to open the MLflow Compare View (Day 036).

    Check the Models tab to see FraudClassifier version 1 (Days 025 & 030).


Day 01:
- create a venv
    This could be done using the `uv` in the Makefile or manually:
    ```
    python3 -m venv
    ```
    To start using the virtual environment:
    ```
    source .venv/bin/activate
    ```
- install and record the requirements in a file
    ```
    uv pip install numpy pandas scikit-learn matplotlib
    ```
    ```
    uv pip freeze > requirements.txt
    ```
    

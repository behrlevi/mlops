import pandas as pd
import mlflow
from mlflow.tracking import MlflowClient

# Connect to the local MLflow tracking server
mlflow.set_tracking_uri("http://localhost:5000")
client = MlflowClient()

# Retrieve the specific experiment by its name
experiment = client.get_experiment_by_name("fraud-signature")

# Search for the most recent run in this experiment
latest_run = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["attributes.start_time DESC"],
    max_results=1
)[0]

# Load the PyFunc model associated with the latest run
model_uri = f"runs:/{latest_run.info.run_id}/model"
loaded_model = mlflow.pyfunc.load_model(model_uri)

# Display the model's schema requirements
print("signature:\n", loaded_model.metadata.signature)

# Test 1: Valid Input
# This DataFrame matches the exact column names the model was trained on
valid_input = pd.DataFrame({"amount": [10.0], "num_txn": [2]})
print("\ngood ->", loaded_model.predict(valid_input))

# Test 2: Invalid Input (Schema Enforcement Test)
# This DataFrame is missing the 'num_txn' column
try:
    invalid_input = pd.DataFrame({"amount": [10.0]})
    loaded_model.predict(invalid_input)
    print("bad  -> NOT enforced")
except Exception as e:
    print("bad  -> rejected:", type(e).__name__)
import sys
import numpy as np
import mlflow
import mlflow.sklearn
from mlflow import MlflowClient
from sklearn.dummy import DummyClassifier

TRACKING_URI = "http://localhost:5000"
EXPERIMENT_NAME = "fraud-detection"

SEED_RUNS = [
    {
        "label": "baseline",
        "params": {"n_estimators": 100, "max_depth": 5},
        "metrics": {"accuracy": 0.82, "f1_score": 0.80},
    },
    {
        "label": "improved",
        "params": {"n_estimators": 200, "max_depth": 10},
        "metrics": {"accuracy": 0.91, "f1_score": 0.89},
    },
]


def _dummy_fit():
    """Return a DummyClassifier fitted on a trivial two-row array —
    a real sklearn estimator with no real learning.
    Used only to satisfy the requirements so the script doen't crash."""
    X = np.array([[0.0], [1.0]])
    y = np.array([0, 1])
    return DummyClassifier(strategy="most_frequent").fit(X, y)

def main():
    mlflow.set_tracking_uri(TRACKING_URI)
    client = MlflowClient()

    existing = client.get_experiment_by_name(EXPERIMENT_NAME)
    if existing is not None and len(client.search_runs([existing.experiment_id])) >= len(SEED_RUNS):
        # Re-spawn safety: seed already populated.
        sys.exit(0)

    mlflow.set_experiment(EXPERIMENT_NAME)

    for cfg in SEED_RUNS:
        with mlflow.start_run(run_name=cfg["label"]):
            mlflow.log_params(cfg["params"])
            for key, value in cfg["metrics"].items():
                mlflow.log_metric(key, value)
            mlflow.sklearn.log_model(_dummy_fit(), name="model")


if __name__ == "__main__":
    main()

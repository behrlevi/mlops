"""Seed the MLflow Model Registry with a `fraud-detector` entry whose
`champion` alias points at a trivial sklearn estimator. The serve lab
resolves this alias at load time.

No real training — a DummyClassifier fitted on a two-row
deterministic array (with two input features) stands in for a trained
estimator. The lab teaches model-serving plumbing, not model quality
(§2.5).
"""
import sys
import numpy as np
import mlflow
import mlflow.sklearn
from mlflow import MlflowClient
from sklearn.dummy import DummyClassifier

TRACKING_URI = "http://localhost:5000"
EXPERIMENT_NAME = "fraud-detection"
MODEL_NAME = "fraud-detector"


def _dummy_fit():
    X = np.array([[0.0, 0.0], [1.0, 1.0]])
    y = np.array([0, 1])
    return DummyClassifier(strategy="most_frequent").fit(X, y)


def main():
    mlflow.set_tracking_uri(TRACKING_URI)
    client = MlflowClient()

    # Re-spawn safety: if the champion alias is already resolvable, skip.
    try:
        existing = client.get_model_version_by_alias(MODEL_NAME, "champion")
    except Exception:
        existing = None
    if existing is not None:
        sys.exit(0)

    mlflow.set_experiment(EXPERIMENT_NAME)

    with mlflow.start_run() as run:
        mlflow.log_param("model_type", "baseline")
        mlflow.log_metric("f1_score", 0.85)
        mlflow.sklearn.log_model(_dummy_fit(), name="model")

    result = mlflow.register_model(
        f"runs:/{run.info.run_id}/model", MODEL_NAME
    )
    client.set_registered_model_alias(MODEL_NAME, "champion", result.version)


if __name__ == "__main__":
    main()
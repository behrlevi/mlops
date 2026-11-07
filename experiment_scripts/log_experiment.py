"""

The model and data in this script are synthetic. A trivial
DummyClassifier stands in for a trained model so that the MLflow
logging calls have a real sklearn estimator to persist, and the
accuracy/F1 scores are computed from its predictions on a small fixed
fixture — not hardcoded. The purpose is to practise the
MLflow logging API, not to reason about model quality.

"""
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, f1_score

mlflow.set_tracking_uri("http://localhost:5000")

# Hyperparameters the run should record as MLflow parameters.
params = {"n_estimators": 100, "max_depth": 5, "random_state": 42}

# Synthetic "trained" model — a DummyClassifier fit on a small set of
# deterministic rows so it has valid internal state for
# mlflow.sklearn.log_model to serialise. No real learning takes place.
X_fit = np.array([[0.0], [1.0], [2.0], [3.0]])
y_fit = np.array([1, 1, 1, 0])
model = DummyClassifier(strategy="most_frequent").fit(X_fit, y_fit)

# Evaluation scores computed from the model's own predictions on the
# fixture above — deterministic and reproducible (accuracy 0.75,
# f1_score ~0.857), not fabricated constants.
preds = model.predict(X_fit)
accuracy = accuracy_score(y_fit, preds)
f1 = f1_score(y_fit, preds)

with mlflow.start_run():
    mlflow.log_params(params)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("f1_score", f1)
    mlflow.sklearn.log_model(model, name="model")

    print(f"accuracy={accuracy}, f1_score={f1}")


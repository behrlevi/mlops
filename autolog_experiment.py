import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression

mlflow.set_tracking_uri("http://localhost:5000")

mlflow.sklearn.autolog()
mlflow.set_experiment("autolog-demo")

# Synthetic four-row XOR-like array. Not a real ML dataset — just
# a deterministic toy to give sklearn.fit() something to execute.
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 1, 1])

model = LogisticRegression(C=1.0, max_iter=100, random_state=42)
model.fit(X, y)

print("Autolog run complete — check the MLflow UI")


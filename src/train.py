import os
import random
import numpy as np
import pandas as pd
import yaml
import mlflow
import mlflow.sklearn
import optuna
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
from mlflow.models import infer_signature

# 1. Environment & MLflow Endpoint Configuration (Day 020 & 029)
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:8333"
os.environ["AWS_ACCESS_KEY_ID"] = "any"
os.environ["AWS_SECRET_ACCESS_KEY"] = "any"

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("Fraud_Detection_Bakeoff") # Day 022


# 2. Seed Discipline Function (Day 032)
def set_seed(seed: int = 42):
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)


def objective(trial, X, y, seed):
    # Parameter Search Space (Day 035)
    n_estimators = trial.suggest_int("n_estimators", 20, 100)
    max_depth = trial.suggest_int("max_depth", 3, 10)

    # Stratified K-Fold (Day 034)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=seed
    )

    scores = cross_val_score(model, X, y, cv=cv, scoring="f1")
    mean_f1 = scores.mean()

    # Log child run inside Optuna trial
    with mlflow.start_run(nested=True):
        mlflow.log_params(trial.params)
        mlflow.log_metric("cv_f1_score", mean_f1)

    return mean_f1


def main():
    # Load config (Day 031)
    with open("params.yaml", "r") as f:
        config = yaml.safe_load(f)

    seed = config["train"]["seed"]
    set_seed(seed)

    # Synthetic Dummy Data for local lab execution
    from sklearn.datasets import make_classification
    X_raw, y_raw = make_classification(n_samples=1000, n_features=10, random_state=seed)
    X = pd.DataFrame(X_raw, columns=[f"feat_{i}" for i in range(10)])
    y = pd.Series(y_raw)

    # Optuna Hyperparameter Optimization (Day 035)
    study = optuna.create_study(direction="maximize")
    
    with mlflow.start_run(run_name="Optuna_Parent_Run"):
        mlflow.log_param("tuning_engine", "Optuna")
        study.optimize(lambda trial: objective(trial, X, y, seed), n_trials=5)

        # Train Champion Model with best params (Day 030 & 036)
        best_params = study.best_params
        champion_model = RandomForestClassifier(**best_params, random_state=seed)
        champion_model.fit(X, y)

        # Log Model Signature (Day 026)
        signature = infer_signature(X, champion_model.predict(X))

        # Register Champion Model (Day 025 & 030)
        mlflow.sklearn.log_model(
            sk_model=champion_model,
            artifact_path="champion_model",
            signature=signature,
            registered_model_name="FraudClassifier"
        )
        mlflow.log_metrics({"best_f1_score": study.best_value})
        print(f"Training Complete. Best F1: {study.best_value:.4f}")

if __name__ == "__main__":
    main()

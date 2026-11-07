"""
MLflow model serving — two TODO blocks wire a pyfunc wrapper with
custom preprocessing around the registered champion model and run a
batch prediction on the pre-staged synthetic input file.

The `ScaledPredictor` class skeleton (constructor + the pyfunc
`predict` signature) is provided; the reader authors the
preprocessing body of `.predict()` and the serving plumbing
(loading the registry champion by alias, wiring it into the pyfunc
wrapper, producing a predictions CSV).

The input file at /root/code/data/inputs.csv is a deterministic
synthetic 10-row numeric batch. No real ML workflow; the prediction
values carry no meaning beyond "the pyfunc ran end to end".
"""
import numpy as np
import pandas as pd
import mlflow
import mlflow.pyfunc

MODEL_URI = "models:/fraud-detector@champion"
INPUT_CSV = "../data/raw/inputs.csv"
OUTPUT_CSV = "../data/processed/predictions.csv"


class ScaledPredictor(mlflow.pyfunc.PythonModel):

    def __init__(self, inner_model, mean, std):
        self.model = inner_model
        self.mean = mean
        self.std = std

    def predict(self, context, model_input, params=None):
        X = np.asarray(model_input, dtype=float)
        scaled = (X - self.mean) / self.std
        return self.model.predict(scaled)
        # Applies the wrapper's per-column scaling to X — subtracts
        # this instance's mean and divides by its std — then returns the
        # inner model's predictions on the scaled array.


mlflow.set_tracking_uri("http://localhost:5000")

inner_model = mlflow.pyfunc.load_model(MODEL_URI)
# Loads the champion version of the `fraud-detector` registered
# model from MLflow and binds the loaded model to `inner_model`.

# Compute per-column mean and std from the pre-staged inputs, then
# build the pyfunc wrapper around `inner_model`.
inputs = pd.read_csv(INPUT_CSV)
mean = inputs.values.mean(axis=0)
std = inputs.values.std(axis=0)
std[std == 0] = 1.0  # guard against division by zero on constant columns

predictor = ScaledPredictor(inner_model, mean, std)

inputs["prediction"] = predictor.predict(None, inputs.values)
inputs.to_csv(OUTPUT_CSV, index=False)
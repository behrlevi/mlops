# Logging experiments

I have added a log_experiment.py to root to test the MLFlow
tracking server without much computation overhead a real ML
model would introduce.
The `DummyClassifier(strategy="most_frequent")` simply looks at
the `.fit` 4-row dataset and guesses the most common class.

As a little detour, just to make things clear, `x_fit` represents
the features, or inputs fed into the model and `y_fit! holds the
lables or the classes. So in case of a fraud detection model,
X would hold some features of an e-mai, and Y if its a spam or not.

The main goal here is to understand how to log hyperparameters,
metrics and artifacts in an experiment.
Take a look at the lines under `with mlflow.start_run():`.

Start the MLFlow server, run the Python script and observe
how these values can be read in the web UI under experiments ->
default -> training runs. Select the latest run and you will
see the parameters are recorded with it.
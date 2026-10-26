# MLflow autologging

The autologging feature replaces the current, boilerplate log_experiment.py.
After implementing `mlflow.sklearn.autolog()` MLflow automatically records
all records in the subsequent model training runs `estimator.fit(...) -
they don't need to be specified in the script.
`mlflow.set_experiment(...)` has to be declared before the fit runs.

Try running `autolog_experiment.py` and a take a look at the run in the GUI.
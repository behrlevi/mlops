# Day 15
## parameter-driven reporducibility

Using a separate parameters file gives you the advantage being able to tune the parameters
without having to touch the source code.

Take a look at `src/models/train.py` which is using the value of `n_estimators`.
We are going to use this as an example.

`params.yaml` holds the value of `n_estimators`
We need to add this as a parameters in `dvc.yaml`

Try to change the value in params.yaml now and run the following command
to see the differences
```
dvc params diff
```

Try running `dvc repro train` with different values in params.yaml.
Re-running the pipeline records the new value in `dvc.lock`

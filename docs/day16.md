# Track metrics with DVC

We would like to track model training in a reproducible form.
Setting a `metrics:` block in dvc.yaml insted of `outs.`, we can
view model performance value with `dvc metrics show`.
By setting `cache: false` keeps `metrics.json` in Git rather then DVC,
which enables the values accross commits with `dvc metrics diff`.

I have upgraded `src/models/train.py` to write the results to the file.
The parameters are recorded in `params.yaml`.

Try running `dvc repro train` with different `max_depth` values and
observe the `f1_score` and `accuracy` scores.

# Comparing DVC experiments

A DVC experiment is a run of the pipeline with the given parameters.
Since we have set up version control for the training metrics,
we can try to run experiments with different `max_depth` values
and store the results in commits.

You can overwrite the values in `params.yaml`, but it is generally
a good practice to use `dvc exp run --set-param <key>=<value>`.

To make this work I have deleted `metrics.json` from `.gitignore`
and added the file to git. Once the file is tracked you can compare
experiments with `dvc exp show` and promote the best one back
to working tree with `dvc exp apply <name>`, which updates `params.yaml`,
`metrics.json` and the model artefacts to match that run.

You can try setting different values for `max_depth`, which is
esentially the depth of each tree in the random forest. Choosing
low values will cause underfitting, while higher overfitting as
you will see on the `f1_score`.

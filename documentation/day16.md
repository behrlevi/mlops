# Day16
## Track metrics with DVC

From now on, we will be recording the training metrics from `train.py` into metrics.json.
To do so, a metrics section needs to be added to `dvc.yaml`.
Also, by setting cache to false, we are preventing this data from being written into `.dvc/cache`, where DVC will copy all files by default
and add them to .gitignore.
Turning of the cache instructs DVC that the file lives in Git.

Now run `dvc repro train` and subsequently `dvc metrics show`, which will display the metrics.

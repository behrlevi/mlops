# Versioning Datasets with Git and SeaweedFS

Datasets are too larege for Git.
To be able to version control model training,
DVC uses the following files:
.dvc - for storing data tracked with `dvc add`
dvc.lock - for pipeline outputs

These object can be tracked by Git and can be used
to recreate a given model by reverting the desired
commit and running `dvc repro`.
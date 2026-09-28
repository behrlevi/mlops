# Complete DVC Pipeline

A DVC pipeline is a Directed Acyclic Graph (DAG) declared
in `dvc.yaml`. The stages represent the nodes of the graph.
As DVC walks down these stages, it changes the hash values
in `dvc.lock`. Versioning this lock file makes the runs
reproducible. The large artifacts (model, data) are handled
by SeaweedFS.

You can experiment with the pipeline by running `dvc repro`
to reproduce the pipeline with current set of `params.yaml`.
The model produced can be uploaded to the bucket with `dvc push`.
Try re-running the pipeline with different parameters and
comitting the lock file. You can then reproduce various models
by rolling back to previous commits with `git checkout` and running
`dvc checkout`.
Note that `git checkout` restores artifact from `.dvc/cache`, so if
you were happen to clone the repository to another machine, you would
also need to re-run the pipeline with the given parameters to get the
model file.

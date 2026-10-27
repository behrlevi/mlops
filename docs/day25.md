**update:** Fixed S3 bucket authentication in the Docker compose file.
Experiments can now save models in SeaWeed. Turned out Boto3 needs to be installed in the container and a identity
with the appropriate permissions is also required.

# Register, version, manage models

`Model registry` is a central catalogue used for model versioning.

Make sure to create a SeaWeed bucket named`mlflow-artifacts`
before running the script, otherwise it will raise an exeption.
You can do this in the Filer by creating a new folder inside
`buckets`.

Run `seed-model.py` and open experiments in MLflow.
You will see two new experiments with different parameters and metrics.

Try registering a new model from both experiments.
As you can see, MLflow assigns versions to the models based on
the order you add them to the registered model. You also have the
option to assign aliases to the different versions.
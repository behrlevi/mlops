Start Services:
```docker compose up -d```

Install uv:
```curl -LsSf https://astral.sh/uv/install.sh | sh```

Setup Env:
```make setup```

Create a SeaweedFS bucket

The Seaweed dashboard can be accessed at: http://localhost:9333/

You need to create the bucket declared in the Dockerfile as a the default artifact root for this to work.
```
python3 -c "
import boto3
s3 = boto3.client('s3', endpoint_url='http://localhost:8333', aws_access_key_id='any', aws_secret_access_key='any')
s3.create_bucket(Bucket='mlflow-artifacts')
"
```

To view the available buckets:
```
echo "fs.ls /buckets" | podman exec -i seaweedfs weed shell
```

To display the contents of the bucket, use this after you ran the experiment:
```
AWS_ACCESS_KEY_ID=any AWS_SECRET_ACCESS_KEY=any aws s3 ls s3://mlflow-artifacts/ --recursive --endpoint-url http://localhost:8333
```
Execute Pipeline:
```python3 src/train.py.```

MLflow UI at http://localhost:5000

    You will see the Fraud_Detection_Bakeoff experiment.

    Select runs to open the MLflow Compare View (Day 036).

    Check the Models tab to see FraudClassifier version 1 (Days 025 & 030).


### Day 01:
- create a venv
    This could be done using the `uv` in the Makefile or manually:
    ```
    python3 -m venv
    ```
    To start using the virtual environment:
    ```
    source .venv/bin/activate
    ```
- install and record the requirements in a file
    ```
    uv pip install numpy pandas scikit-learn matplotlib
    ```
    ```
    uv pip freeze > requirements.txt
    ```

### Day 02:

Using Jupyter Notebook.
Jupyter Lab is already installed in the venv. Activate is and run:

```
nohup jupyter lab --config=./jupyter_lab_config.py --allow-root --no-browser > /tmp/jupyter.log 2>&1 &
```

### Day 03:

Use the following command to create a .txt from requirements.ini file listing the names of the packages (one per line)
and optionally their pinned versions
```
uv pip compile requirements.in -o requirements.txt
```

### Day 04:

Introducing a `.gitignore` file
A .gitignore tells Git which paths to leave untracked, but it has no effect on files already committed.
We will create a list of files to exclude Python caches, trained model files, the virtual environment,
notebook checkpoints and local secrets from the commits.

To list files currently tracked by git
```
git ls-files
```

To untrack already-commited artifacts
```
git rm -r --cached
```
You need to provide the paths for this command like this
```
git rm -r --cached src/__pycache__ models/fraud_model.pkl venv
```

In order to implement the cleanup, .gitignore file needs to be added to the stagin area
```
git add .gitignore
```



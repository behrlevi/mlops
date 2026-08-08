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

### Day 05:
The Makefile

The purpose of the file is to streamline the bulk execution of commands. You can create stages of operations and execute them
with `make setup`, etc. You an even create groups holding multiple stages as `all: setup lint`, etc.

The `.PHONY:` target serves to distinguish stages from filenames so `make` does not execute files named setup or lint created
in the root directory.
More technically: The names following it are treated as its prerequisites.
Make registers every prerequisite of .PHONY in its internal table as a non-file rule, instructing the dependency graph to ignore
disk checks for those names and always run their recipe.

### Day 06:
Linters

For ensuring code quality, we are going to utilize Ruff and Black.
`Black` is only a formatter, whereas `Ruff` is a linter/formatter.
The first only adjustst the code to conform with the universal style
requirements and has minimal adjustable settings.
The later does linting - scanning the code for bugs, logic errors, etc. -
and formats the code like `Black`.
Historically they were used together, but Ruff has a Black-compatible formatter
which makes concurrent usage unecessary. I'm leaving both in though for reference
and to provide the user with the choice to decide.

You can try them out with:
```
# linter in safe mode
ruff check src/
# linter
ruff check --fix src/
# formatter in safe mode
ruff format --check src/
# formatter
ruff format src/
```
and
```
# safe mode
black --check src/
# live
black src/
```

Please observe the setting in `pyproject.toml`.
The linters will automatically check this file and grab the settings from it.
In case of ruff, we are applying four rules:
"W" - style warnings (structural style issues and syntax errors - whitespace, line breaaks, etc)
"E" - style errors (enforcing the PEP style guide)
"F" - Pyflakes linter (logical errors and bugs)
"I" - isort (sorting and groping imports)

### Day 07:
Testing and packaging

We have two goals to achieve in the section.
The first is to write a simple unit test and run it.
The second is to package the application into a portable and reproduciblewheel (.whl),
which holds the source code and all the dependecies and can be set up everywhere with pip.

1. I have written the test logic in src/fraud_detection/predict.py which return 1 if the first value exceeds 100 and 0
if its below.
When `python3 -m pytest tests/ -q` is executed, [tool.pytest.ini_options] is read from `pyproject.toml`,
which sets pythonpath to the src directory. It executes src/tests/test_predict.py, which in turn
imports and executes the logic from src/fraud_detection/prediction.py.
The two tests should pass with the following output:
```
..                                                                                                [100%]
2 passed in 0.00s
```

2. The wheel can be built with `python3 -m build`.
Python spins up an isolated, temporary environment for building the package.
It reads `[build-system]` from `pyproject.toml` and outputs two files in the dist directory:
```
fraud_detection-0.1.0-py3-none-any.whl
fraud_detection-0.1.0.tar.gz
```
You should try deploying the .whl from another directory with:
```
pip install ../dist/fraud_detection-0.1.0-py3-none-any.whl
```
Then open a python3 terminal and run the following:
```
import fraud_detection
print(fraud_detection.__version__)
```
Note:
If you run Python from inside your repository folder, it will just read your local src/ directory instead of the installed package.

### Day 08:
pre-commit

`pre-commit` is a framework which runs small checks (hooks) commits automatically.
The configuration needs to be defines in a `.pre-commit-config.yaml` file placed in the
root directory. The file contains the hooks defined by `repo` - the URL of the remote repo,
` rev` - version, and a `hook` - the id of the hook.
Using pre-commit allows us to wire automated checks to enforce code quality.

Test it out by creating a new commit or with

```
pre-commit run --all-files
```

To keep hook version up-to-date, use:
```
pre-commit autoupdate
```

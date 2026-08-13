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

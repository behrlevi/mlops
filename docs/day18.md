# Version datasets accross branches

Since Git only versions the .lock files and the large datasets are handled by DVC, we need to learn
how to manage different versions of the models using Git branches.

You can try out a simple experiment.
Image that you acquire a new dataset you can train you model on and you wish to do it on a separate branch.
Copy current dataset
```
cp data/raw/transactions.csv data/raw/transactions_v2.csv
```
and make some adjustments to new dataset - delete some of the lines from it to make this easy.

Add a simple tag to current commit to pin the state.
```
git tag v.1.0
```

Create a new branch and switch to it.
```
git branch v2
git switch v2
```

Replace the old dataset with the new, add it to dvc and re-run the pipeline.
```
cp data/raw/transactions_v2.csv /data/raw/transactions.csv
dvc add data/raw/transactions.csv
dvc repro
```
A new transactions.dvc file will be created which holds the current state of the dataset.

Switch back to the main branch with `git switch main` and open `transaction.csv`.
You will see that it still has the modified content of v2.
Remember, that git ignores the dataset as they are too big for this VCS.

To re-generate the original `transactions.csv`, run `dvc checkout`.

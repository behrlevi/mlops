# Day 11
Track a dataset with DVC

Big datasets should not be stored in the git repository.
We will use DVC to handle them.

We will be working with a sample set stored in `/data/raw`.

The first step is to make sure `transactions.csc` is untracked by git.
```
git rm -r --cached data/raw/transactions.csv
```
We can list tracked files with
```
git ls-files
```
To track a file with DVC
```
dvc add dvc add data/raw/transactions.csv
```
By executing this command, DVC move the file to .dvc/cache and creates
a symlink in the original location pointing to the cache.
You can inspect `.dvc/cache/files/md5/d0/839c183f4b657bbdd411a57e397cf1`
to see that is has the same content as the original transactions.csv.

After adding the file, DVC will also create an entry in .gitignore and
instruct you to add this newly created .dvc pointer file and also .gitingore.

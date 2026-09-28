# Running a DVC pipeline

A DVC pipeline is used to record data manipulation steps for future reference so they don't have to be remembered.
It relies on a `dvc.yaml` file - the documentation can be found here: https://doc.dvc.org/user-guide/project-structure/dvcyaml-files

We are going to create a simple pipeline with two stages.
The first stage `pocess_data`, sanitizes the data. The script
reads transactions.csv, removes duplicates and N/A-s and saves the
cleansed data in the data/processed directory.
The second stage `split_data`, randomly distributes the data between
two files, leaving 20% for testing and the rest for training.

The stages in the DVC configuration file can be called with:
```
dvc repro <stage_name>
```
Executing `dvc repro` loops thorugh all stages.

Once it's finished, the output will prompt you to add the dvc.lock
to git.
The lock file is used to store the current state of the pipeline
after it has been successfully executed. It records the MD5 hash
values of the files managed by DVC. This connects git version control
with the DVC repository and the commit is thus tied to a certain state
of the data. When you need to roll-back to a given point, `git checkout`
will restore the lock file and subsequenty running `dvc checkout` reads
the hashes in `dvc.lock` and links the corresponding file back into the
workspace from the local `.dvc/cache`.

After `dvc push` you can open the Filer and see that the new .cvs files
were uploaded to SeaweedFS. It is worhwile to notice that the files in
the bucket are created from the first two letters of the hash value
and the rest of the value is used as the filename.

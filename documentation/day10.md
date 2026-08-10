# Initizialzing DVC

Data Version Control is used to version large files like datasets and models.
Traditional Git is not ideal for these big files and we are only using it to
for keeping a record of the files and the configuration in .dvc and .dvcignore
configs, while the actual data is pushed to a bucket storage like SeaweedFS.

To initialize the repository:
```
dvc init
```

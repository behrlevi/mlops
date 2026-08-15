# Day12
Push to SeaWeedFS

SeaWeed is an S3 compatible storage we are going to use to store
data tracked by DVC.
You can access the master node interface can be accessed at:
http://localhost:9333
and the Filer at http://localhost:8888

The configuration file is located at `.dvc/config`.
In it you have to specify the path of the bucket (url),
the hostname of the SeaWeed server (endpointurl) and the credetials
(we are using the default username and password).
You can also modify these values with the CLI
```
dvc remote default s3
dvc remote modify s3 endpointurl http://localhost:8333
dvc remote modify s3 url s3://dvc-storage
```
Make sure you have created the bucket, which you can do easily with
the Filer.

If everything is set, you can upload the data to bucket
```
dvc push
```

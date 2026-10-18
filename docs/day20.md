# Running MLFlow server

The task was to run the server using the command
```
mlflow server \
  --backend-store-uri sqlite:////root/code/mlflow-backend/mlflow.db \
  --default-artifact-root /root/code/mlflow-artifacts \
  --host 0.0.0.0 \
  --port 5000 \
  --allowed-hosts '*' \
  --cors-allowed-origins '*' &
  ```

Mlfow needs the following directories to store the SQLite database (metadata store)
and artifact directory.
```
mkdir -p /root/code/mlflow-backend /root/code/mlflow-artifacts
```

In this particular repository, I'm using Docker to run the server.
import os

# path to GCP-credentials
SERVICE_ACCOUNT_PATH = os.path.join("..", ".gcp", "gcs-user-key.json")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_PATH

from google.cloud import storage
import os

from data_loader.config import config as cfg

# --- load configurations ---
cfg.set_gcp_credentials()
conf = cfg.load()

BUCKET_NAME = conf['storage']['bucket']
DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data", "raw", "jaffle-data"
)

def upload_files_to_gcs(data_dir, bucket_name, prefix="raw"):
    """loads all files in the data directory to a GCS bucket"""
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    for file_name in os.listdir(data_dir):
        local_path = os.path.join(data_dir, file_name)
        if os.path.isfile(local_path):  # only files
            blob = bucket.blob(f"{prefix}/{file_name}")
            blob.upload_from_filename(local_path)
            print(f"Uploaded: {file_name}")


if __name__ == "__main__":
    upload_files_to_gcs(DATA_DIR, BUCKET_NAME)

import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from google.cloud import storage
import config.config

client = storage.Client()
for bucket in client.list_buckets():
    print(bucket.name)


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"{source_file_name} uploaded to {destination_blob_name}.")

upload_blob(
    "my-data-lake-bucket",         # Bucketname
    "local_file.csv",              # Lokale Datei
    "raw/local_file.csv"           # Zielpfad in GCS
)
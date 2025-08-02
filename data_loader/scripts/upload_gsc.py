import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from google.cloud import storage
import config.config

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "raw", "jaffle-data")

client = storage.Client()
bucket = client.bucket("jaffle-files")

for file_name in os.listdir(DATA_DIR):
    local_path = os.path.join(DATA_DIR, file_name)
    if os.path.isfile(local_path):  # exclude directories
        blob = bucket.blob(f"raw/{file_name}")
        blob.upload_from_filename(local_path)
        print(f"uploaded: {file_name}")

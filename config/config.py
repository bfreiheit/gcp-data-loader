import os
import sys

# path to GCP-credentials
SERVICE_ACCOUNT_PATH = os.path.join("..", ".gcp", "gcs-user-key.json")

# check if file exists
if not os.path.exists(SERVICE_ACCOUNT_PATH):
    sys.stderr.write(f"credentials not found: {SERVICE_ACCOUNT_PATH}\n")
    sys.exit(1)

# check if file is readable
if not os.access(SERVICE_ACCOUNT_PATH, os.R_OK):
    sys.stderr.write(f"no reading permission: {SERVICE_ACCOUNT_PATH}\n")
    sys.exit(1)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_PATH

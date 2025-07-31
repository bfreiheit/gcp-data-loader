# gcp-data-loader

This repository uses the Python library [`jafgen`](https://pypi.org/project/jafgen/) to generate synthetic datasets, 
stores them in **Google Cloud Storage (GCS)**, and then loads them into **Google BigQuery**.

---

## Project Structure

├── README.md
├── config
│   ├── config.py
│   └── config.yaml
├── data
│   └── raw
│       └── jaffle-data
│           ├── raw_customers.csv
│           ├── raw_items.csv
│           ├── raw_orders.csv
│           ├── raw_products.csv
│           ├── raw_stores.csv
│           ├── raw_supplies.csv
│           └── raw_tweets.csv
├── requirements.txt
└── scripts
    ├── generate_data.py
    ├── load_bigquery.py
    └── upload_gsc.py

## Installation and Usage

### 1. Clone the repository
```bash
git clone git@github.com:bfreiheit/gcp-data-loader.git
cd gcp-data-loader
``` 

### 2. Setup a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python packages

```bash
pip install -r requirements.txt
```

### 4. Switch to data folder and import jaffles files

```bash
cd data/raw
jafgen 2
```

## Configuration
All project settings (e.g., GCP bucket name, BigQuery dataset) are defined in:
config/config.yaml


from google.cloud import bigquery

from data_loader.config import config as cfg


# --- load configurations ---
cfg.set_gcp_credentials()
conf = cfg.load()

BUCKET_NAME = conf['storage']['bucket']
DATASET_ID = conf['bigquery']['dataset_id']
TABLES = conf['tables']

def get_bq_client():   
    return bigquery.Client()

def build_gcs_uri(table_info): 
    return f"gs://{BUCKET_NAME}/{table_info['path']}"

def build_schema(table_info):
    """builds schema from config.yaml"""
    return [bigquery.SchemaField(**field) for field in table_info.get('schema', [])] or None

def build_job_config(table_info, schema):
    """creates the Bigquery config"""
    job_config = bigquery.LoadJobConfig(
        schema=schema,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

    if 'partition_field' in table_info:
        job_config.time_partitioning = bigquery.TimePartitioning(
            field=table_info['partition_field'],
            type_=bigquery.TimePartitioningType.DAY
        )
    return job_config


def load_table(bq_client, table_name, table_info):
    """loads one table from GSC to Bigquery"""
    gcs_uri = build_gcs_uri(table_info)
    print(f"Loading table {table_name} from {gcs_uri}...")

    schema = build_schema(table_info)
    job_config = build_job_config(table_info, schema)

    load_job = bq_client.load_table_from_uri(
        gcs_uri,
        f"{DATASET_ID}.{table_name}",
        job_config=job_config
    )
    load_job.result()
    print(f"Table {table_name} successfully loaded with {load_job.output_rows} rows.")


def load_tables_from_gcs():
    """loads all tables to Bigquery"""
    bq_client = get_bq_client()  

    for table_name, table_info in TABLES.items():
        load_table(bq_client, table_name, table_info)    


if __name__ == "__main__":
    load_tables_from_gcs()

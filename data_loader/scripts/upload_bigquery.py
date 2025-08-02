import yaml
import importlib.resources as pkg_resources

from google.cloud import bigquery, storage

from data_loader.config import config


config.set_gcp_credentials()

# load yaml   
config = config.load()

bucket_name = config['storage']['bucket']
dataset_id = config['bigquery']['dataset_id']
tables = config['tables']

print(bucket_name)

bq_client = bigquery.Client()
storage_client = storage.Client()

def load_tables_from_gcs():
    for table_name, table_info in tables.items():
        gcs_uri = f"gs://{bucket_name}/{table_info['file_path']}"
        print(f"load tables {table_name} from {gcs_uri}...")

        schema = [bigquery.SchemaField(**field) for field in table_info.get('schema', [])]

        job_config = bigquery.LoadJobConfig(
            schema=schema if schema else None,
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
        )

        if 'partition_field' in table_info:
            job_config.time_partitioning = bigquery.TimePartitioning(
                field=table_info['partition_field'],
                type_=bigquery.TimePartitioningType.DAY
            )

        load_job = bq_client.load_table_from_uri(
            gcs_uri,
            f"{dataset_id}.{table_name}",
            job_config=job_config
        )
        load_job.result()  # Warten bis Job abgeschlossen
        print(f"table {table_name} successfully loaded with {load_job.output_rows} rows.")


'''  
if __name__ == "__main__":
    load_tables_from_gcs()

'''



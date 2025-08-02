from data_loader.config import config

def test_load_tables_from_gcs():
    cfg = config.load()
    bucket_name = cfg["storage"]["bucket"]
    tables = cfg["tables"]     

    for table_name, table_info in tables.items():
        
        assert f"gs://{bucket_name}/{table_info['path']}" == f"gs://jaffle-files/raw/{table_name}.csv"



import yaml
import os
import importlib.resources as pkg_resources

def load() -> dict:
    with pkg_resources.files(__package__).joinpath("config.yaml").open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def set_gcp_credentials() -> str:
    cfg = load()
    cred_path = os.path.expanduser(cfg['gcp']['credentials_path'])
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred_path
    return cred_path # only for depugging


from data_loader.config import config

def test_load_returns_expected_keys():
    cfg = config.load()
    assert isinstance(cfg, dict)
    assert "storage" in cfg
    assert "tables" in cfg

from src.storage import ResultStorage
import os

def test_storage_creates_db():
    storage = ResultStorage()
    assert os.path.exists("data/results.db")

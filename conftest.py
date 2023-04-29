import pytest
from src.Database import Database

VALUE = 3

@pytest.fixture()
def database():
    database = Database(size=VALUE)
    yield database
    database.rm_cache()
import pytest
from src.Database import Database


@pytest.mark.parametrize("value", [-1, 0])
def test_size_negative(value):
    with pytest.raises(ValueError):
        Database(size=value)


def test_last_element_to_be_first(database):
    database.add(10)
    database.add(50)
    database.add(100)
    assert database.data[0] == 100

def test_last_elem(database):
    database.add(10)
    database.add(50)
    database.add(100)
    database.add(500)
    assert database.data[-1] != 10

def test_positive_numbers(database):
    database.add(-1)
    database.add(0)
    database.add(2)
    database.add(1)
    assert len(database.data) == 2

def test_empty_string(database):
    database.add('')
    assert len(database.data) == 0

def test_string(database):
    database.add('123')
    assert len(database.data) == 1


import calc

## Configure test and choose pytest

def test_add():
    assert calc.add(3, 2) == 5

def test_subtract():
    assert calc.subtract(5, 2) == 3
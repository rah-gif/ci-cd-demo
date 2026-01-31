from app import add, calculate_total

def test_add():
    assert add(2, 3) == 5

def test_calculate():
    assert calculate_total(100, 10) == 110
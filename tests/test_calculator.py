from calculator import add, subtract

def test_addition():
    assert add(5,7) == 12

def test_subtraction():
    assert subtract(10,5) == 5    

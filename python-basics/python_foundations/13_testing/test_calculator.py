import pytest
from calculator import add, divide

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

@pytest.mark.parametrize("a,b,expected", [(1,2,3), (0,0,0), (-1,1,0)])
def test_add_cases(a,b,expected):
    assert add(a,b) == expected

import pytest
from calculator import square
def test_pos():
    assert square(2)==4

def test_neg():
    assert square(-3)==9

def test_zero():
    assert square(0)==0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

if __name__=="__main__":
    pytest.main()
from functions import add,subtract, multiply
from functions import convert_fahr_to_c as f2c
import pytest
def test_add():
	assert add(2,3) ==5
	assert add("space","ship")=="spaceship"


def test_subtract():
	assert subtract(2,3)==-1

def test_covert_fahr_to_c():
	assert f2c(32)==0
	assert f2c(122)== pytest.approx(50)
 	with pytest.raises (AssertionError)
		f2c(-600)

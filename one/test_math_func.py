import math_func
import pytest
import sys


@pytest.mark.number
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(2) == 4
    assert math_func.add(5) == 7


@pytest.mark.number
def test_multiple():
    assert math_func.multipl(5, 5) == 25
    assert math_func.multipl(3) == 6
    assert math_func.multipl(1) == 2


@pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello ', 'World')
    #print(result)
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hemdkf' not in result


#@pytest.mark.skip(reason="do not run it")
@pytest.mark.skipif(sys.version_info > (3, 1), reason="too old python")
def test_multiple_strings():
    assert math_func.multipl('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.multipl('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result

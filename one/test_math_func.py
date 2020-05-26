import math_func


def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(2) == 4
    assert math_func.add(5) == 7


def test_multiple():
    assert math_func.multipl(5, 5) == 25
    assert math_func.multipl(3) == 6
    assert math_func.multipl(1) == 2


def test_add_strings():
    result = math_func.add('Hello ', 'World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hemdkf' not in result

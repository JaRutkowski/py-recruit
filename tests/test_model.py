import pytest
from model import CalculatorModel






def test_add():
    calc = CalculatorModel()
    result = calc.add(2, 3)
    assert result == 5


def test_subtract():
    calc = CalculatorModel()
    result = calc.subtract(5, 2)
    assert result == 3


def test_multiply():
    calc = CalculatorModel()
    result = calc.multiply(2, 3)
    assert result == 6


def test_divide():
    calc = CalculatorModel()
    result = calc.divide(10, 2)
    assert result == 5


def test_divide_by_zero():
    calc = CalculatorModel()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)

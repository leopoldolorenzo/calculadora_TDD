import pytest
from src.calculator import Calculator

def test_addition():
    calc = Calculator()
    assert calc.add(1, 2) == 3

def test_subtraction():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3



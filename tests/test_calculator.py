import pytest
from src.calculator import Calculadora

def test_sumar():
    calc = Calculadora()
    assert calc.sumar(1, 2) == 3

def test_restar():
    calc = Calculadora()
    assert calc.restar(5, 2) == 3

def test_multiplicar():
    calc = Calculadora()
    assert calc.multiplicar(3, 2) == 6

def test_dividir():
    calc = Calculadora()
    assert calc.dividir(6, 2) == 3
    with pytest.raises(ValueError):
        calc.dividir(6, 0)

def test_raiz_cuadrada():
    calc = Calculadora()
    assert abs(calc.raiz_cuadrada(9) - 3) < 0.001
    assert abs(calc.raiz_cuadrada(2) - 1.414) < 0.001

def test_exponencial():
    calc = Calculadora()
    assert abs(calc.exponencial(1) - 2.718) < 0.001
    assert abs(calc.exponencial(0) - 1) < 0.001
    assert abs(calc.exponencial(2) - 7.389) < 0.001
    assert abs(calc.exponencial(-1) - 0.367) < 0.001    
    
# Run the tests
# $ pytest tests/test_calculator.py

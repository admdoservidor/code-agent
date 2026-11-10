# tests/test_calculadora.py
"""Testes unitários para a classe Calculadora (calculadora.py).

Os testes cobrem:
- soma
- subtração
- multiplicação
- divisão
- tentativa de divisão por zero (deve levantar ValueError)
"""

import pytest
from calculadora import Calculadora


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (1, 2, 3),                # inteiros positivos
        (-1, -5, -6),             # inteiros negativos
        (3.5, 2.1, 5.6),          # floats
        (0, 0, 0),                # zeros
        (-2.5, 4, 1.5),           # misto negativo/positivo
    ],
)
def test_somar(a, b, esperado):
    """Verifica que Calculadora.somar retorna a soma correta."""
    assert Calculadora.somar(a, b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (5, 3, 2),                # inteiros positivos
        (-2, -4, 2),              # inteiros negativos
        (7.2, 2.5, 4.7),          # floats
        (0, 5, -5),               # zero menos positivo
        (-3.5, 1.5, -5.0),        # misto negativo/positivo
    ],
)
def test_subtrair(a, b, esperado):
    """Verifica que Calculadora.subtrair retorna a diferença correta (a - b)."""
    assert Calculadora.subtrair(a, b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (2, 3, 6),                # inteiros positivos
        (-2, -4, 8),              # inteiros negativos
        (1.5, 4, 6.0),            # floats
        (0, 10, 0),               # zero multiplicado
        (-3, 5, -15),             # misto negativo/positivo
    ],
)
def test_multiplicar(a, b, esperado):
    """Verifica que Calculadora.multiplicar retorna o produto correto."""
    assert Calculadora.multiplicar(a, b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (6, 3, 2.0),              # inteiros positivos
        (-8, -2, 4.0),            # inteiros negativos
        (7.5, 2.5, 3.0),          # floats
        (0, 5, 0.0),              # zero dividido por algo
        (-9, 3, -3.0),            # misto negativo/positivo
    ],
)
def test_dividir(a, b, esperado):
    """Verifica que Calculadora.dividir retorna a divisão correta (float)."""
    assert Calculadora.dividir(a, b) == esperado


def test_dividir_por_zero():
    """Dividir por zero deve levantar ValueError com a mensagem correta."""
    with pytest.raises(ValueError) as excinfo:
        Calculadora.dividir(10, 0)
    assert str(excinfo.value) == "Divisão por zero não é permitida."

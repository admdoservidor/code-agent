# Testes unitários para a classe Calculadora.

import pytest
from calculadora import Calculadora


def test_somar():
    assert Calculadora.somar(2, 3) == 5
    assert Calculadora.somar(-1, 5) == 4
    assert Calculadora.somar(2.5, 4.1) == pytest.approx(6.6)


def test_subtrair():
    assert Calculadora.subtrair(10, 4) == 6
    assert Calculadora.subtrair(5, 10) == -5
    assert Calculadora.subtrair(-3, -2) == -1


def test_multiplicar():
    assert Calculadora.multiplicar(3, 4) == 12
    assert Calculadora.multiplicar(-2, 5) == -10
    assert Calculadora.multiplicar(0, 100) == 0
    assert Calculadora.multiplicar(2.5, 4) == pytest.approx(10.0)


def test_dividir():
    assert Calculadora.dividir(10, 2) == 5.0
    assert Calculadora.dividir(-9, 3) == -3.0
    assert Calculadora.dividir(7, 2) == pytest.approx(3.5)


def test_dividir_por_zero():
    with pytest.raises(ValueError) as exc:
        Calculadora.dividir(5, 0)
    assert "Divisão por zero não é permitida" in str(exc.value)


def test_operacoes_com_tipos_invalidos():
    # Qualquer operação que não suporte os operadores aritméticos deve
    # gerar TypeError (ex.: somar strings não é suportado aqui).
    with pytest.raises(TypeError):
        Calculadora.somar("a", "b")
    with pytest.raises(TypeError):
        Calculadora.subtrair([1, 2], 3)
    with pytest.raises(TypeError):
        Calculadora.multiplicar(None, 5)
    with pytest.raises(TypeError):
        Calculadora.dividir("10", 2)

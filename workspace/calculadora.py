# calculadora.py
"""Módulo que contém a classe Calculadora.

A classe oferece operações aritméticas básicas (soma, subtração,
multiplicação e divisão) com suporte a type hints e tratamento de erro
para divisão por zero.
"""

from __future__ import annotations


class Calculadora:
    """Classe que implementa operações aritméticas simples.

    Todos os métodos são estáticos porque não há necessidade de manter
    estado entre as chamadas. Cada método recebe dois operandos do tipo
    ``float`` (ou qualquer tipo que suporte as operações aritméticas) e
    devolve o resultado também como ``float``.
    """

    @staticmethod
    def somar(a: float, b: float) -> float:
        """Retorna a soma de *a* e *b*.

        >>> Calculadora.somar(2, 3)
        5
        """
        return a + b

    @staticmethod
    def subtrair(a: float, b: float) -> float:
        """Retorna a diferença entre *a* e *b* (a - b).

        >>> Calculadora.subtrair(5, 2)
        3
        """
        return a - b

    @staticmethod
    def multiplicar(a: float, b: float) -> float:
        """Retorna o produto de *a* e *b*.

        >>> Calculadora.multiplicar(4, 2.5)
        10.0
        """
        return a * b

    @staticmethod
    def dividir(a: float, b: float) -> float:
        """Retorna a divisão de *a* por *b*.

        Levanta ``ValueError`` se *b* for zero para evitar ``ZeroDivisionError``
        não tratado.

        >>> Calculadora.dividir(10, 2)
        5.0
        """
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b

import math


class Calculadora:

    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):

        if b == 0:
            raise ValueError("Divisão por zero")

        return a / b


def calcular_raiz(valor):
    return math.sqrt(valor)

def calcular_media(valores):
    return sum(valores) / len(valores)
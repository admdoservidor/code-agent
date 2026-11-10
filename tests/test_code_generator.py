from code_agent.tools.code_generator import validar_codigo_python

def test_codigo_valido():
    codigo = """
def somar(a, b):
    return a + b
"""

    resultado = validar_codigo_python.invoke({
        "codigo": codigo
    })

    assert "sintaticamente válido" in resultado


def test_codigo_com_erro_sintatico():
    codigo = """
def somar(a, b)
    return a + b
"""

    resultado = validar_codigo_python.invoke({
        "codigo": codigo
    })

    assert "erro de sintaxe" in resultado.lower()
    assert "Linha: 2" in resultado


def test_codigo_vazio():
    resultado = validar_codigo_python.invoke({
        "codigo": ""
    })

    assert "Nenhum código" in resultado


def test_codigo_com_classe():
    codigo = """
class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
"""

    resultado = validar_codigo_python.invoke({
        "codigo": codigo
    })

    assert "sintaticamente válido" in resultado

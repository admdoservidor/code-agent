from code_agent.tools.error_analyzer import extrair_informacoes

def test_identifica_zero_division_error():
    traceback_texto = """
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    resultado = calcular(10, 0)
  File "main.py", line 5, in calcular
    return a / b
ZeroDivisionError: division by zero
"""

    resultado = extrair_informacoes(traceback_texto)

    assert resultado["tipo"] == "ZeroDivisionError"
    assert resultado["mensagem"] == "division by zero"


def test_identifica_localizacao():
    traceback_texto = """
Traceback (most recent call last):
  File "main.py", line 5, in calcular
    return a / b
ZeroDivisionError: division by zero
"""

    resultado = extrair_informacoes(traceback_texto)

    assert resultado["localizacao"]["arquivo"] == "main.py"
    assert resultado["localizacao"]["linha"] == 5
    assert resultado["localizacao"]["funcao"] == "calcular"


def test_traceback_vazio():
    resultado = extrair_informacoes("")

    assert resultado["tipo"] == "Erro não identificado"
    assert resultado["localizacao"] is None

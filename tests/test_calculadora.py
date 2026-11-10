def somar(a, b):
    return a + b

def test_somar():
    assert somar(2, 3) == 5

def test_somar_com_negativos():
    assert somar(-2, -3) == -5
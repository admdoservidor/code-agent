
import ast
import textwrap

from code_agent.tools.code_analysis import CodeAnalyzer


def test_identifica_funcao():
    codigo = textwrap.dedent("""
        def somar(a, b):
            return a + b
    """)

    arvore = ast.parse(codigo)

    analyzer = CodeAnalyzer()
    analyzer.visit(arvore)

    assert "somar" in analyzer.functions


def test_identifica_classe():
    codigo = textwrap.dedent("""
        class Pessoa:
            pass
    """)

    arvore = ast.parse(codigo)

    analyzer = CodeAnalyzer()
    analyzer.visit(arvore)

    assert "Pessoa" in analyzer.classes


def test_identifica_condicional():
    codigo = textwrap.dedent("""
        if True:
            print("Olá")
    """)

    arvore = ast.parse(codigo)

    analyzer = CodeAnalyzer()
    analyzer.visit(arvore)

    assert analyzer.conditionals == 1

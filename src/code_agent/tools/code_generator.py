import ast
from langchain.tools import tool

@tool
def validar_codigo_python(codigo: str) -> str:
    """
    Valida a sintaxe de um código Python sem executá-lo.
    """

    if not codigo.strip():
        return "Nenhum código foi informado."

    if len(codigo) > 100_000:
        return "O código ultrapassa o limite de 100 KB."

    try:
        ast.parse(codigo)
        return (
            "Código Python sintaticamente válido. "
            "Nenhuma execução foi realizada."
        )

    except SyntaxError as erro:
        return "\n".join([
            "Código Python com erro de sintaxe.",
            f"Tipo: {type(erro).__name__}",
            f"Linha: {erro.lineno}",
            f"Coluna: {erro.offset}",
            f"Descrição: {erro.msg}",
        ])

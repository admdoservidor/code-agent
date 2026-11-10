import ast
from langchain.tools import tool
from code_agent.tools.project import validar_caminho

class CodeAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.functions = []
        self.classes = []
        self.imports = []
        self.loops = 0
        self.conditionals = 0
        self.try_blocks = 0

    def visit_FunctionDef(self, node):
        self.functions.append(node.name)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.functions.append(node.name)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.classes.append(node.name)
        self.generic_visit(node)

    def visit_Import(self, node):
        for item in node.names:
            self.imports.append(item.name)

    def visit_ImportFrom(self, node):
        self.imports.append(node.module or "")

    def visit_For(self, node):
        self.loops += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.loops += 1
        self.generic_visit(node)

    def visit_If(self, node):
        self.conditionals += 1
        self.generic_visit(node)

    def visit_Try(self, node):
        self.try_blocks += 1
        self.generic_visit(node)


@tool
def analisar_codigo(caminho: str) -> str:
    """Analisa a estrutura sintática de um arquivo Python."""

    try:
        arquivo = validar_caminho(caminho)

        if not arquivo.is_file():
            return "Arquivo não encontrado."

        if arquivo.suffix != ".py":
            return "Apenas arquivos Python são aceitos."

        if arquivo.stat().st_size > 100_000:
            return "Arquivo muito grande para análise."

        codigo = arquivo.read_text(encoding="utf-8")
        arvore = ast.parse(codigo, filename=str(arquivo))
        analyzer = CodeAnalyzer()
        analyzer.visit(arvore)

        resultado = [
            f"Arquivo: {caminho}",
            f"Funções: {analyzer.functions}",
            f"Classes: {analyzer.classes}",
            f"Imports: {analyzer.imports}",
            f"Loops: {analyzer.loops}",
            f"Condicionais: {analyzer.conditionals}",
            f"Blocos try: {analyzer.try_blocks}",
        ]
        return "\n".join(resultado)

    except SyntaxError as erro:
        return (
            f"Erro de sintaxe na linha {erro.lineno}: "
            f"{erro.msg}"
        )

    except (ValueError, OSError, UnicodeDecodeError):
        return "Não foi possível analisar o arquivo."

from pathlib import Path
from langchain.tools import tool
from code_agent.core.config import PROJECT_ROOT


DIRETORIOS_IGNORADOS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    ".pytest_cache",
    ".mypy_cache",
}

PADROES_TESTE = (
    "test_*.py",
    "*_test.py",
)



def localizar_arquivos_teste() -> list[Path]:
    encontrados = set()

    for padrao in PADROES_TESTE:
        for arquivo in PROJECT_ROOT.rglob(padrao):
            relativo = arquivo.relative_to(PROJECT_ROOT)

            if any(
                parte in DIRETORIOS_IGNORADOS
                for parte in relativo.parts
            ):
                continue

            if arquivo.is_file():
                encontrados.add(arquivo)

    return sorted(encontrados)



@tool
def descobrir_testes(modulo: str = "") -> str:
    """
    Descobre arquivos de teste pytest no workspace.
    Pode filtrar testes relacionados a um módulo, como calculadora.
    """

    if len(modulo) > 200:
        return "O nome do módulo informado é muito longo."

    arquivos = localizar_arquivos_teste()

    if not arquivos:
        return (
            "Nenhum arquivo de teste foi encontrado no workspace. "
            "Procure arquivos com padrão test_*.py ou *_test.py."
        )

    if modulo.strip():
        termo = modulo.strip().lower()
        relacionados = []

        for arquivo in arquivos:
            nome = arquivo.stem.lower()

            try:
                conteudo = arquivo.read_text(
                    encoding="utf-8"
                ).lower()
            except (OSError, UnicodeDecodeError):
                continue

            if termo in nome or termo in conteudo:
                relacionados.append(arquivo)

        arquivos = relacionados

        if not arquivos:
            return (
                f"Nenhum teste relacionado a '{modulo}' "
                "foi encontrado."
            )

    caminhos = [
        str(arquivo.relative_to(PROJECT_ROOT))
        for arquivo in arquivos
    ]

    return (
        f"Arquivos de teste encontrados: {len(caminhos)}\n\n"
        + "\n".join(caminhos)
    )

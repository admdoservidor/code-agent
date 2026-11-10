
from pathlib import Path
from langchain.tools import tool
from code_agent.core.config import PROJECT_ROOT

IGNORAR = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules"
}

def validar_caminho(caminho: str) -> Path:
    """Impede acesso fora do workspace."""

    raiz = PROJECT_ROOT.resolve()
    arquivo = (raiz / caminho).resolve()

    if not arquivo.is_relative_to(raiz):
        raise ValueError("Acesso fora do workspace não permitido.")

    return arquivo

@tool
def listar_arquivos() -> str:
    """Lista arquivos disponíveis no projeto."""

    arquivos = []

    for arquivo in PROJECT_ROOT.rglob("*"):

        if not arquivo.is_file():
            continue

        relativo = arquivo.relative_to(PROJECT_ROOT)

        if any(parte in IGNORAR for parte in relativo.parts):
            continue

        arquivos.append(str(relativo))

        if len(arquivos) >= 200:
            break

    if not arquivos:
        return "Nenhum arquivo encontrado."

    return "\n".join(arquivos)

@tool
def ler_arquivo(caminho: str) -> str:
    """Lê um arquivo de texto dentro do workspace."""

    try:
        arquivo = validar_caminho(caminho)

        if not arquivo.is_file():
            return "Arquivo não encontrado."

        if arquivo.stat().st_size > 100_000:
            return "Arquivo muito grande para leitura."

        return arquivo.read_text(encoding="utf-8")

    except UnicodeDecodeError:
        return "Não foi possível interpretar o arquivo como UTF-8."

    except (ValueError, OSError):
        return "Não foi possível acessar o arquivo."

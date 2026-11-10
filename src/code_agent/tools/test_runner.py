
import subprocess
import sys

from pathlib import Path
from langchain.tools import tool

from code_agent.core.config import PROJECT_ROOT
from code_agent.tools.project import validar_caminho


TEMPO_MAXIMO = 30
TAMANHO_MAXIMO_RESULTADO = 15_000


@tool
def executar_testes(caminho: str) -> str:
    """
    Executa um arquivo de testes pytest dentro do workspace.
    Exige autorização explícita do usuário.
    """

    if not caminho.strip():
        return "Informe o caminho do arquivo de testes."

    try:
        arquivo = validar_caminho(caminho)

        if not arquivo.is_file():
            return "Arquivo de testes não encontrado."

        if arquivo.suffix != ".py":
            return "Apenas arquivos Python podem ser executados."

        if not arquivo.name.startswith("test_"):
            return "O arquivo deve começar com 'test_'."

        print("\n" + "=" * 50)
        print("AUTORIZAÇÃO PARA EXECUÇÃO DE TESTES")
        print("=" * 50)
        print(f"Arquivo: {arquivo}")
        print(f"Tempo máximo: {TEMPO_MAXIMO} segundos")
        print("=" * 50)

        confirmacao = input(
            "\nDeseja executar esse arquivo? Digite SIM: "
        ).strip()

        if confirmacao != "SIM":
            return "Execução cancelada pelo usuário."

        comando = [
            sys.executable,
            "-m",
            "pytest",
            "-q",
            str(arquivo.relative_to(PROJECT_ROOT)),
        ]

        processo = subprocess.run(
            comando,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=TEMPO_MAXIMO,
            shell=False,
            check=False,
        )

        saida = processo.stdout
        erros = processo.stderr

        resultado = (saida + "\n" + erros).strip()

        if len(resultado) > TAMANHO_MAXIMO_RESULTADO:
            resultado = (
                resultado[:TAMANHO_MAXIMO_RESULTADO]
                + "\n\n[Resultado truncado]"
            )

        if processo.returncode == 0:
            status = "TESTES CONCLUÍDOS COM SUCESSO"
        else:
            status = (
                f"TESTES FINALIZADOS COM FALHAS "
                f"(código {processo.returncode})"
            )

        return "\n".join([
            status,
            "",
            resultado or "Nenhuma saída produzida.",
        ])

    except subprocess.TimeoutExpired:
        return (
            f"Tempo máximo de execução excedido "
            f"({TEMPO_MAXIMO} segundos)."
        )

    except FileNotFoundError:
        return (
            "Não foi possível iniciar o pytest. "
            "Verifique se está instalado no ambiente Python."
        )

    except (ValueError, OSError) as erro:
        return f"Não foi possível executar os testes: {erro}"

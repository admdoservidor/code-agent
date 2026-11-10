from langchain.tools import tool
from code_agent.tools.project import validar_caminho

TAMANHO_MAXIMO = 100_000

EXTENSOES_PERMITIDAS = {
    ".py",
    ".txt",
    ".md",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".html",
    ".css",
    ".js",
    ".ts",
}


@tool
def criar_arquivo(caminho: str, conteudo: str) -> str:
    """
    Cria um novo arquivo de texto dentro do workspace.
    Solicita confirmação no terminal e nunca sobrescreve arquivos.
    """

    if not caminho.strip():
        return "Informe o caminho do arquivo."

    if len(conteudo) > TAMANHO_MAXIMO:
        return "O conteúdo ultrapassa o limite de 100 KB."

    try:
        arquivo = validar_caminho(caminho)

        if arquivo.suffix.lower() not in EXTENSOES_PERMITIDAS:
            return "Extensão não permitida para criação."

        if arquivo.exists():
            return (
                "O arquivo já existe. "
                "Nenhuma alteração foi realizada."
            )

        print("\n" + "=" * 50)
        print("PROPOSTA DE CRIAÇÃO DE ARQUIVO")
        print("=" * 50)
        print(f"Caminho: {arquivo}")
        print("\nConteúdo proposto:\n")
        print(conteudo)
        print("=" * 50)

        confirmacao = input(
            "\nDeseja criar esse arquivo? Digite SIM para confirmar: "
        ).strip()

        if confirmacao != "SIM":
            return "Operação cancelada pelo usuário."

        arquivo.parent.mkdir(parents=True, exist_ok=True)

        # Modo x: cria o arquivo somente se ele ainda não existir.
        with arquivo.open("x", encoding="utf-8") as destino:
            destino.write(conteudo)

        return f"Arquivo criado com sucesso: {caminho}"

    except FileExistsError:
        return (
            "O arquivo já existe. "
            "Nenhuma alteração foi realizada."
        )

    except (ValueError, OSError) as erro:
        return f"Não foi possível criar o arquivo: {erro}"

import re
from langchain.tools import tool

def extrair_informacoes(traceback_texto: str) -> dict:
    """Extrai informações importantes de um traceback Python."""

    linhas = traceback_texto.strip().splitlines()
    arquivos = re.findall(r'File "([^"]+)", line (\d+), in ([^\n]+)', traceback_texto)
    excecoes = re.findall(r"^([A-Za-z_][\w.]*(?:Error|Exception|Warning)):\s*(.*)$", traceback_texto, re.MULTILINE)

    if excecoes:
        tipo_erro, mensagem = excecoes[-1]
    else:
        tipo_erro = "Erro não identificado"
        mensagem = "Não foi possível identificar a exceção."

    ultimo_arquivo = None

    if arquivos:
        caminho, numero_linha, funcao = arquivos[-1]
        ultimo_arquivo = {
            "arquivo": caminho,
            "linha": int(numero_linha),
            "funcao": funcao,
        }

    return {
        "tipo": tipo_erro,
        "mensagem": mensagem,
        "localizacao": ultimo_arquivo,
        "quantidade_frames": len(arquivos),
        "ultima_linha": linhas[-1] if linhas else "",
    }

@tool
def analisar_erro(traceback_texto: str) -> str:
    """
    Analisa um traceback Python e identifica a exceção,
    sua mensagem e a localização provável do erro.
    """

    if not traceback_texto.strip():
        return "Nenhum traceback foi informado."

    if len(traceback_texto) > 50_000:
        return "O traceback é muito grande para análise."

    resultado = extrair_informacoes(traceback_texto)

    localizacao = resultado["localizacao"]

    if localizacao:
        arquivo = localizacao["arquivo"]
        linha = localizacao["linha"]
        funcao = localizacao["funcao"]
    else:
        arquivo = "Não identificado"
        linha = "Não identificada"
        funcao = "Não identificada"

    return "\n".join([
        "ANÁLISE DO ERRO",
        f"Tipo: {resultado['tipo']}",
        f"Mensagem: {resultado['mensagem']}",
        f"Arquivo: {arquivo}",
        f"Linha: {linha}",
        f"Função: {funcao}",
        f"Frames encontrados: {resultado['quantidade_frames']}",
    ])

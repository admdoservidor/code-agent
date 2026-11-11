from langchain.agents import create_agent
from code_agent.llm.provider import get_llm
from code_agent.core.prompts import CODING_SYSTEM_PROMPT
from code_agent.tools.project import listar_arquivos, ler_arquivo
from code_agent.tools.code_analysis import analisar_codigo
from code_agent.tools.error_analyzer import analisar_erro
from code_agent.tools.code_generator import validar_codigo_python
from code_agent.tools.file_editor import criar_arquivo
from code_agent.tools.test_runner import executar_testes
from code_agent.tools.test_discovery import descobrir_testes

def create_coding_agent(checkpointer=None):

    return create_agent(
        model=get_llm(),
        tools=[
            listar_arquivos,
            ler_arquivo,
            analisar_codigo,
            analisar_erro,
            validar_codigo_python,
            criar_arquivo,
            executar_testes,
            descobrir_testes,
        ],
        system_prompt=CODING_SYSTEM_PROMPT,
        checkpointer=checkpointer
    )
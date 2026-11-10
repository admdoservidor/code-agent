from langchain.agents import create_agent
from code_agent.llm.provider import get_llm
from code_agent.core.prompts import CODING_SYSTEM_PROMPT
from code_agent.tools.project import listar_arquivos, ler_arquivo
from code_agent.tools.code_analysis import analisar_codigo

def create_coding_agent(checkpointer=None):

    return create_agent(
        model=get_llm(),
        tools=[
            listar_arquivos,
            ler_arquivo,
            analisar_codigo
        ],
        system_prompt=CODING_SYSTEM_PROMPT,
        checkpointer=checkpointer
    )
from langchain.agents import create_agent

from code_agent.llm.provider import get_llm
from code_agent.core.prompts import CODING_SYSTEM_PROMPT
from code_agent.tools.project import listar_arquivos, ler_arquivo

def create_coding_agent(checkpointer=None):

    llm = get_llm()
    
    tools = [
        listar_arquivos,
        ler_arquivo
    ]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=CODING_SYSTEM_PROMPT,
        checkpointer=checkpointer
    )

    return agent
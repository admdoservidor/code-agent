from langchain_groq import ChatGroq

from code_agent.core.config import (
    GROQ_API_KEY,
    GROQ_MODEL
)

def get_llm():

    return ChatGroq(
        model=GROQ_MODEL,
        api_key=GROQ_API_KEY,
        temperature=0
    )
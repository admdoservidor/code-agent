from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from code_agent.core.config import GROQ_API_KEY, GROQ_MODEL
from code_agent.core.config import GEMINI_API_KEY, GEMINI_MODEL


def get_llm():

    return ChatGroq(
        model=GROQ_MODEL,
        api_key=GROQ_API_KEY,
        temperature=0
    )
    return ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        google_api_key=GEMINI_API_KEY,
        temperature=0.7,
    )



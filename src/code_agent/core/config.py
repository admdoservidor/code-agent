import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[3]

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-20b"
)

PROJECT_ROOT = Path(
    os.getenv("PROJECT_ROOT", "./workspace")
).resolve()

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY não configurada.")

PROJECT_ROOT.mkdir(parents=True, exist_ok=True)
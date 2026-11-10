from pathlib import Path
from contextlib import contextmanager
from langgraph.checkpoint.sqlite import SqliteSaver

@contextmanager
def get_checkpointer():
    # Localiza a raiz do projeto
    project_root = Path(__file__).resolve().parents[3]

    # Define o diretório e cria caso não exista
    data_dir = project_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    # Caminho do banco SQLite
    db_path = data_dir / "checkpoints.sqlite"

    # Abre o checkpointer
    with SqliteSaver.from_conn_string(str(db_path)) as checkpointer:
        yield checkpointer
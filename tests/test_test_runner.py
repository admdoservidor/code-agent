
from code_agent.tools.test_runner import executar_testes


def configurar_workspace(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "code_agent.tools.project.PROJECT_ROOT",
        tmp_path,
    )

    monkeypatch.setattr(
        "code_agent.tools.test_runner.PROJECT_ROOT",
        tmp_path,
    )


def test_cancela_execucao(monkeypatch, tmp_path):
    configurar_workspace(monkeypatch, tmp_path)

    arquivo = tmp_path / "test_exemplo.py"
    arquivo.write_text(
        "def test_exemplo():\n    assert True\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "NAO",
    )

    resultado = executar_testes.invoke({
        "caminho": "test_exemplo.py"
    })

    assert "cancelada" in resultado


def test_rejeita_arquivo_sem_prefixo(monkeypatch, tmp_path):
    configurar_workspace(monkeypatch, tmp_path)

    arquivo = tmp_path / "exemplo.py"
    arquivo.write_text(
        "print('teste')",
        encoding="utf-8",
    )

    resultado = executar_testes.invoke({
        "caminho": "exemplo.py"
    })

    assert "deve começar com 'test_'" in resultado


def test_rejeita_arquivo_inexistente(monkeypatch, tmp_path):
    configurar_workspace(monkeypatch, tmp_path)

    resultado = executar_testes.invoke({
        "caminho": "test_inexistente.py"
    })

    assert "não encontrado" in resultado

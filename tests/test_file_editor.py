from code_agent.tools.file_editor import criar_arquivo

def configurar_workspace(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "code_agent.tools.project.PROJECT_ROOT",
        tmp_path,
    )


def test_cria_arquivo_com_autorizacao(monkeypatch, tmp_path):
    configurar_workspace(monkeypatch, tmp_path)

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "SIM",
    )

    resultado = criar_arquivo.invoke({
        "caminho": "teste.py",
        "conteudo": "print('Olá mundo')",
    })

    arquivo = tmp_path / "teste.py"

    assert arquivo.exists()
    assert arquivo.read_text(encoding="utf-8") == "print('Olá mundo')"
    assert "criado com sucesso" in resultado


def test_cancela_criacao(monkeypatch, tmp_path):
    configurar_workspace(monkeypatch, tmp_path)

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "NAO",
    )

    resultado = criar_arquivo.invoke({
        "caminho": "teste.py",
        "conteudo": "print('Olá mundo')",
    })

    assert not (tmp_path / "teste.py").exists()
    assert "cancelada" in resultado


def test_nao_sobrescreve_arquivo(monkeypatch, tmp_path):
    configurar_workspace(monkeypatch, tmp_path)

    arquivo = tmp_path / "existente.py"
    arquivo.write_text("valor = 10", encoding="utf-8")

    resultado = criar_arquivo.invoke({
        "caminho": "existente.py",
        "conteudo": "valor = 20",
    })

    assert arquivo.read_text(encoding="utf-8") == "valor = 10"
    assert "já existe" in resultado


def test_impede_acesso_fora_workspace(monkeypatch, tmp_path):
    configurar_workspace(monkeypatch, tmp_path)

    resultado = criar_arquivo.invoke({
        "caminho": "../arquivo.py",
        "conteudo": "print('teste')",
    })

    assert "Não foi possível criar" in resultado


def test_rejeita_extensao_nao_permitida(monkeypatch, tmp_path):
    configurar_workspace(monkeypatch, tmp_path)

    resultado = criar_arquivo.invoke({
        "caminho": "programa.exe",
        "conteudo": "conteudo",
    })

    assert "Extensão não permitida" in resultado

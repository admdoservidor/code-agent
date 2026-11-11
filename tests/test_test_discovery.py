from code_agent.tools.test_discovery import descobrir_testes


def test_encontra_arquivos_de_teste(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "code_agent.tools.test_discovery.PROJECT_ROOT",
        tmp_path,
    )

    pasta = tmp_path / "tests"
    pasta.mkdir()

    (pasta / "test_calculadora.py").write_text(
        "def test_somar():\n    assert 1 + 1 == 2",
        encoding="utf-8",
    )

    resultado = descobrir_testes.invoke({})

    assert "test_calculadora.py" in resultado


def test_filtra_por_modulo(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "code_agent.tools.test_discovery.PROJECT_ROOT",
        tmp_path,
    )

    pasta = tmp_path / "tests"
    pasta.mkdir()

    (pasta / "test_calculadora.py").write_text(
        "def test_somar():\n    assert True",
        encoding="utf-8",
    )

    (pasta / "test_usuario.py").write_text(
        "def test_usuario():\n    assert True",
        encoding="utf-8",
    )

    resultado = descobrir_testes.invoke({
        "modulo": "calculadora"
    })

    assert "test_calculadora.py" in resultado
    assert "test_usuario.py" not in resultado


def test_nao_encontra_testes(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "code_agent.tools.test_discovery.PROJECT_ROOT",
        tmp_path,
    )

    resultado = descobrir_testes.invoke({})

    assert "Nenhum arquivo de teste" in resultado

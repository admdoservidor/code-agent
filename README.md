# Code Agent

**AI Coding Agent** construído com [LangChain](https://langchain.com/), [LangGraph](https://langchain-ai.github.io/langgraph/) e [Groq](https://groq.com/).

Um assistente de programação interativo que cria arquivos, analisa código, valida Python, executa testes e analisa erros — tudo dentro de um workspace isolado, com memória de conversação persistente via SQLite.

> **Versão:** 0.1.0  
> **Python:** `>=3.11`

---

## ✨ Funcionalidades

- 💬 **Chat interativo** no terminal com memória de conversação (checkpointer SQLite).
- 📁 **Criação de arquivos** no workspace (com confirmação explícita e sem sobrescrever).
- 🔍 **Leitura e listagem** de arquivos do projeto.
- 🧪 **Execução de testes** (pytest) e análise de resultados.
- 🐛 **Análise de erros** e sugestões de correção.
- ✅ **Validação de código Python** antes de gravar no disco.
- 🧠 **Memória persistente** por identificador de conversa (`thread_id`).
- 🔒 **Segurança:** operações restritas ao diretório `./workspace`, tamanho máximo de 100 KB por arquivo e extensões permitidas.

---

## 🛠 Stack tecnológica

| Camada | Tecnologia |
|--------|------------|
| Orquestração de agentes | LangGraph, LangChain |
| Modelo de linguagem | Groq (`openai/gpt-oss-20b` por padrão) |
| Memória | `langgraph-checkpoint-sqlite` |
| Ambiente | Python 3.11+, `python-dotenv` |
| Qualidade de código | Ruff |
| Testes | Pytest |

---

## 🚀 Como começar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/code-agent.git
cd code-agent
```

### 2. Crie o ambiente virtual

O projeto usa [uv](https://github.com/astral-sh/uv):

```bash
uv sync
```

Ou, com `venv` + `pip`:

```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
# source .venv/bin/activate  # Linux/macOS
pip install -e .
```

### 3. Configure as variáveis de ambiente

Copie o arquivo de exemplo e preencha sua chave da Groq:

```bash
copy .env.example .env       # Windows
# cp .env.example .env       # Linux/macOS
```

Edite o `.env`:

```env
GROQ_API_KEY=sua_chave_aqui
GROQ_MODEL=openai/gpt-oss-20b
PROJECT_ROOT=./workspace
```

> Obtenha sua chave em [console.groq.com](https://console.groq.com/).

### 4. Execute o agente

```bash
uv run main
# ou
python -m code_agent.main
```

Ao iniciar, informe um identificador de conversa (ex: `projeto-python`). Digite suas solicitações em português. Para encerrar, digite `sair`, `exit` ou `quit`.

Exemplo de interação:

```
Identificador da conversa (ex: projeto-python): meu-projeto

Code Agent iniciado!
Digite 'sair' para encerrar.

Você: Crie uma calculadora simples em Python com soma, subtração, multiplicação e divisão.

Code Agent: ...
```

---

## 🧰 Ferramentas disponíveis

| Ferramenta | O que faz |
|------------|-----------|
| `listar_arquivos` | Lista os arquivos do workspace. |
| `ler_arquivo` | Lê o conteúdo de um arquivo. |
| `analisar_codigo` | Analisa qualidade e possíveis problemas no código. |
| `analisar_erro` | Recebe uma mensagem de erro e sugere correções. |
| `validar_codigo_python` | Valida sintaxe Python antes de salvar. |
| `criar_arquivo` | Cria um novo arquivo no workspace (solicita confirmação `SIM`). |
| `executar_testes` | Executa a suíte de testes do projeto. |

---

## 📂 Estrutura do projeto

```
code-agent/
├── .env                # Variáveis de ambiente (não versionado)
├── .env.example        # Exemplo de variáveis de ambiente
├── .gitignore
├── pyproject.toml      # Metadados e dependências
├── uv.lock             # Lockfile do uv
├── README.md
├── data/               # Checkpoints SQLite (memória)
├── src/
│   └── code_agent/
│       ├── main.py             # Ponto de entrada (CLI)
│       ├── agents/
│       │   └── coding_agent.py # Definição do agente LangGraph
│       ├── core/
│       │   ├── config.py       # Configurações
│       │   └── prompts.py      # Prompts do sistema
│       ├── llm/
│       │   └── provider.py     # Provedor de LLM (Groq)
│       ├── memory/
│       │   └── checkpointer.py # Memória SQLite
│       ├── services/
│       │   └── conversation.py
│       └── tools/
│           ├── code_analysis.py
│           ├── code_generator.py
│           ├── error_analyzer.py
│           ├── file_editor.py
│           ├── project.py
│           └── test_runner.py
├── tests/              # Testes do agente
└── workspace/          # Diretório de trabalho dos projetos criados
```

---

## ⚠️ Segurança e boas práticas

- O agente só opera dentro do diretório definido em `PROJECT_ROOT` (padrão: `./workspace`).
- A criação de arquivos **exige confirmação** digitando `SIM` no terminal.
- Arquivos existentes **nunca são sobrescritos**.
- Tamanho máximo de conteúdo por arquivo: **100 KB**.
- Extensões permitidas: `.py`, `.txt`, `.md`, `.json`, `.yaml`, `.yml`, `.toml`, `.html`, `.css`, `.js`, `.ts`.
- Nunca commite o arquivo `.env` (ele está no `.gitignore`).

---

## 🧪 Testes

Execute a suíte de testes com pytest:

```bash
uv run pytest
# ou
pytest
```

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Desenvolvido com 🚀 usando LangChain, LangGraph e Groq.
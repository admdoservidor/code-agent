from code_agent.agents.coding_agent import create_coding_agent
from code_agent.memory.checkpointer import get_checkpointer

def main():

    checkpointer = get_checkpointer()
    agent = create_coding_agent(
        checkpointer=checkpointer
    )

    thread_id = "terminal-session"

    print("=" * 50)
    print("       CODE AGENT - ASSISTENTE DE CÓDIGO")
    print("=" * 50)
    print("\nDigite 'sair' para encerrar.\n")

    while True:

        pergunta = input("Você: ").strip()

        if not pergunta:
            continue

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Encerrando agente...")
            break

        try:
            resposta = agent.invoke(
                {"messages": [{"role": "user", "content": pergunta}]},
                config={"configurable": {"thread_id": thread_id}}
            )

            mensagem = resposta["messages"][-1]

            print("\nCode Agent:")
            print(mensagem.content)
            print()

        except Exception as erro:
            print(f"\nErro: {erro}\n")


if __name__ == "__main__":
    main()
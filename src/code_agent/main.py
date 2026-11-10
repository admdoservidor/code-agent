from code_agent.agents.coding_agent import create_coding_agent
from code_agent.memory.checkpointer import get_checkpointer

def executar_conversa(agent, thread_id):

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    while True:
        pergunta = input("\nVocê: ").strip()
        if pergunta.lower() in ["sair", "exit", "quit"]:
            break
    
        if not pergunta:
            continue

        try:
            resposta = agent.invoke(
                {"messages": [{"role": "user","content": pergunta}]},
                config=config
            )
            print("\nCode Agent:")
            print(resposta["messages"][-1].content)

        except Exception as erro:
            print(f"\nErro: {erro}")


def main():
    thread_id = input("Identificador da conversa (ex: projeto-python): ").strip()

    if not thread_id:
        print("Identificador obrigatório.")
        return

    with get_checkpointer() as checkpointer:

        agent = create_coding_agent(
            checkpointer=checkpointer
        )

        print("\nCode Agent iniciado!")
        print("Digite 'sair' para encerrar.")

        executar_conversa(agent, thread_id)


if __name__ == "__main__":
    main()
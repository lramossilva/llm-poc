from llm.llama_local import LlamaLocal

def main():
    llm = LlamaLocal(model="llama3")

    print("LLM local pronto. Digite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Pergunta: ")

        if pergunta.lower() in ("sair", "exit"):
            break

        resposta = llm.ask(pergunta)
        print(f"\nResposta:\n{resposta}\n")

if __name__ == "__main__":
    main()
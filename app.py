import streamlit as st

from llm.llama_local import LlamaLocal

llm = LlamaLocal(model="llama3")

def main():
    st.title("LLM Local - CodereviewApp")

    st.write("LLM local pronto. Digite 'sair' para encerrar.\n")

    pergunta = st.text_input("Pergunta:")

    if pergunta:
        if pergunta.lower() in ("sair", "exit"):
            st.write("Encerrando a aplicação.")
            return

        # Aqui você pode chamar a função do LLM para obter a resposta
        resposta = llm.ask(pergunta)
        
        st.write(f"\nResposta:\n{resposta}\n")

if __name__ == "__main__":
    main() 
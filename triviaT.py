import streamlit as st

# Função para verificar a resposta
def check_answer(selected_option):
    if selected_option == 1:
        return "Correto!"
    else:
        return "Errado. A resposta correta é Picasso."

# Configuração da página
st.title("Trivia Time")

# Pergunta
st.write("Which painter was born in Spain?")

# Opções
option = st.radio("Choose an option:", ["Picasso", "Matisse"])

# Botão de submissão
if st.button("Submit"):
    result = check_answer(1 if option == "Picasso" else 2)
    st.write(result)

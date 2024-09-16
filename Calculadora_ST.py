import streamlit as st

# Título do aplicativo
st.title('Calculadora de Descontos')

# Solicita o valor do produto ao usuário
n1 = st.number_input('Coloque o valor do produto aqui: ')

# Solicita a porcentagem de desconto ao usuário
n2 = st.number_input('Coloque a porcentagem de desconto aqui: ')

# Calcula o preço final após aplicar o desconto
soma = n1 - (n1 * n2) / 100

# Mostra o preço do produto, o desconto, e por último qual o preço do produto com o desconto
st.write(f'O produto que era R$ {n1:.2f} com o desconto de {n2} % ficou R$ {soma:.2f}')

# Mostra se o produto está com um bom desconto, abaixo de 500, 300 e 100
if soma > 500:
    st.warning('O preço está altíssimo mesmo com o desconto, não compre!')
elif soma > 300:
    st.warning('O preço está muito alto, espere um desconto melhor!')
elif soma > 100:
    st.info("O desconto está bom, porém ainda está caro!")
else:
    st.success('Com esse desconto o preço está bom, pode comprar!')

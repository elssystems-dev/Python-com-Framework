import streamlit as st
st.title("Problema terreno")

#Entrada de Dados
st.write("Digite a largura do terreno em metros")
largura = st.number_input("Largura (m):")

st.write("Digite o comprimento do terreno em metros")
comprimento = st.number_input("Comprimento (m):")

st.write("Digite o valor do metro quadrado em reais: ")
valor_m2 = st.number_input("Valor do M² (R$):")

# Processamento de dados
area = largura * comprimento
preco = area * valor_m2

# Saída de Dados
st.write(f"A área do terreno é de {area} metros quadrados")
st.write(f"O preço total é R$ {preco}")


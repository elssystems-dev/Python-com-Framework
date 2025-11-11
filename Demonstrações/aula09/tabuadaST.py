import streamlit as st

TITULO = "Tabuada"
st.title(TITULO)
st.set_page_config(TITULO)

multiplicador_max = 10
i = multiplicador_max

numero_digitado = ""

# Entrada de dados
try:
    numero_digitado = int(st.text_input("Digite o número para ser \"tabuado\": ") )

    if st.button("Calcular"):
        st.markdown(f"""               
        | Multiplicadores     | Produtos de {numero_digitado}                |
        |---------------------|----------------------------------------------|
        |  {i-9}              | {numero_digitado * (i-9)}                    | 
        |  {i-8}              | {numero_digitado * (i-8)}                    |
        |  {i-7}              | {numero_digitado * (i-7)}                    |
        |  {i-6}              | {numero_digitado * (i-6)}                    |
        |  {i-5}              | {numero_digitado * (i-5)}                    |
        |  {i-4}              | {numero_digitado * (i-4)}                    |
        |  {i-3}              | {numero_digitado * (i-3)}                    |
        |  {i-2}              | {numero_digitado * (i-2)}                    |
        |  {i-1}              | {numero_digitado * (i-1)}                    |
        |  {i}                | {numero_digitado * (i)}                      |    
        """)
except ValueError:
    if numero_digitado is None:
        st.error("Por favor, digite números inteiros.")
    else:
        st.warning("Digite algum valor!")

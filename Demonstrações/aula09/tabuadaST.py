import streamlit as st

TITULO = "Tabuada"
st.title(TITULO)
st.set_page_config(TITULO)

numero_digitado = ""

# Entrada de dados
try:
    numero_digitado = int(st.text_input("Digite o número para ser \"tabuado\": ") )

    if st.button("Calcular"):
        for i in range(1, 11):
            saida = f"{numero_digitado} x {i} = {numero_digitado * i}"
            st.markdown(f""" 
|{saida}|
|-------|
""")
except ValueError:
    if numero_digitado is None:
        st.error("Por favor, digite números inteiros.")
    else:
        st.warning("Digite algum valor!")

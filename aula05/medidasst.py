import streamlit as st
import math as mt

# Problemas medidas 
TITULO = "Cálculo de área de um quadrado, triângulo e trapézio"
st.set_page_config(page_title=f"{TITULO}")
st.markdown(f"<h1 style='text-align: center; margin-bottom: 10vh;'>{TITULO}</h1>", unsafe_allow_html=True)

# Entrada de dados
medidaA = st.number_input("Inserir medida (Base):")
medidaB = st.number_input("Inserir medida (Altura):")
medidaC = st.number_input("Inserir medida (Base menor):")

# Processamento de dados
areaQuadrado = mt.pow(medidaA, 2)
areaTriangulo = (medidaA * medidaB) / 2
areaTrapezio = ((medidaA + medidaC) * medidaB) / 2

# Saída de dados
st.markdown("<h2 style='text-align: left;'>Resultados:</h2>", unsafe_allow_html=True)
st.write(f"A área do quadrado é: {areaQuadrado:.4f} m²")
st.write(f"A área do triângulo é: {areaTriangulo:.4f} m²")
st.write(f"A área do trapézio é: {areaTrapezio:.4f} m²")
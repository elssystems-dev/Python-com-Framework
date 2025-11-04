import streamlit as st
import math as mt

# Problemas medidas 
TITULO = "Cálcilo de área de um quadrado, triângulo e trapézio"
st.title(TITULO)

# Entrada de dados
medidaA = st.number_input("Inserir medida (Base):")
medidaB = st.number_input("Inserir medida (Altura):")
medidaC = st.number_input("Inserir medida (Base menor):")

# Processamento de dados
areaQuadrado = mt.pow(medidaA, 2)
areaTriangulo = (medidaA * medidaB) / 2
areaTrapezio = ((medidaA + medidaC) * medidaB) / 2

# Saída de dados
st.write(f"A área do quadrado é: {areaQuadrado:.4f}")
st.write(f"A área do triângulo é: {areaTriangulo:.4f}")
st.write(f"A área do trapézio é: {areaTrapezio:.4f}")
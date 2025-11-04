import streamlit as st
import math as mt

# Problema retângulo
st.title("Problema retângulo")

# Entrada de Dados
base = st.number_input("Digite a base do retângulo:", min_value=0.0, format="%.1f")
altura = st.number_input("Digite a altura do retângulo", min_value=0.0, format="%.1f")

#Processamento de dados
area = base * altura
perimetro = 2 * (base +altura )
diagonal = (base ** 2 + altura ** 2)
diagonal = mt.sqrt(diagonal)

# Saída de Dados
st.write(f"A área do retângulo é {area}")
st.write(f"O perímetro do retângulo é {perimetro}")
st.write(f"A diagonal do retângulo é {diagonal}")

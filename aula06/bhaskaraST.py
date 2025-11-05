import streamlit as st
import math as mt

delta = "(esperando dados...)"

st.header('Calculadora de Bháskara')
st.write("alculadora de raízes \n de uma equação de segundo grau")
st.write("ax² + bx + c = 0")


# Entrada de dados
a = st.text_input('Digite o valor de a:')
b = st.text_input('Digite o valor de b:')
c = st.text_input('Digite o valor de c:')

# Processamento de dados
if st.button("Calcular raízes"):
    try:
        a = float(a)
        b= float(b)
        c = float(c)
        delta = mt.pow(b, 2) - 4 * a * c
        if delta < 0:
            st.warning("A equação não possui raízes reais")
        elif delta == 0:
            raiz = round((-b + mt.sqrt(delta)) / (2*a), ndigits=3)
            st.success(f"A equação possui uma raíz real: {raiz}")
        else:
            raiz1 = round((-b + mt.sqrt(delta)) / (2*a), ndigits=3)
            raiz2 = round((-b - mt.sqrt(delta)) / (2*a), ndigits=3)
            st.success(f"As raízes da equação são:\n Raiz 1: {raiz1} \n Raiz 2: {raiz2} ")
    except:
        st.error("Por favor, insira valores válidos para a, b e c.")

st.write("O valor de delta é ", delta)


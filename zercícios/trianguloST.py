import streamlit as st
import math

st.title("Calculadora de Área do Triângulo")

lado1 = st.number_input("Digite o primeiro lado do triângulo: ", icon="🥇", min_value=0.0)
lado2 = st.number_input("Digite o segundo lado do triângulo: ", icon="🥈", min_value=0.0)
lado3 = st.number_input("Digite o terceiro lado do triângulo: ", icon="🥉", min_value=0.0)

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    st.warning("Digite medidas válidas para todos os lados.")
else:
    if st.button("Calcular", icon="➕"):
        perimetro = (lado1 + lado2 + lado3)
        areaTrapezio = ((lado1 + lado2) * lado3) / 2

        if (lado1 + lado2) > lado3 and (lado2 + lado3) > lado1 and (lado3 + lado1) > lado2: # Está dando erro? R: Não, está correto.
            st.success("Os lados inseridos formam um triângulo!")
            st.write(f"O perímetro do triângulo apresentado é {perimetro:.2f}") 
            # Para formar o gráfico do triângulo, seria necessário, no eixo y, estabelecer que o limite é a própria altura
            # do triângulo, desconhecida no momento. Além disso, o vértice mais alto deverá estar no y altura e x (lado1 [ou base] / 2)
            # O segundo vértice poderá começar em  x = 0 e y = 0 , ou mesmo 1 em ambos para melhor visualização, 
            # e o terceiro vértice estará + lado1 distante do segundo vértice.
            # Ou seja, em uma condição streamlit, os segmentos não serão formados através dos pontos do vértice, infelizmente.
        else:
            st.warning("Os lados inseridos não podem formar um triângulo.")
            st.write(f"Por outro lado, a área de um trapézio formado por estas mesmas medidas é {areaTrapezio:.2f}")

        st.divider()
        st.subheader("Gráfico de Barras das Medidas")
        st.bar_chart([lado1, lado2, lado3], use_container_width=True, x_label="Lado", y_label="Medida")
        



import streamlit as st
st.title("🎯 Simulação de lançamento de dardos 🎯")

'''Simulação de lançamento de três dardos. O objetivo do aplicativo é 
mostrar o dardo com a maior distância'''

# Entrada de dados
st.header("Inserir as três distâncias dos dardos lançados pelo jogador:")
coluna1, coluna2, coluna3 = st.columns(3)
with coluna1:
    dardo1 = st.number_input("Distância do 1º dardo", min_value=0.0)
with coluna2:
    dardo2 = st.number_input("Distância do 2º dardo", min_value=0.0)
with coluna3:
    dardo3 = st.number_input("Distância do 3º dardo", min_value=0.0)
maior_distancia = max(dardo1, dardo2, dardo3)

# Estrutura de controle de decisão
if (dardo1 > dardo2) and (dardo1 > dardo3):
    dardo_vencedor = "Dardo 1"
elif (dardo2 > dardo1) and (dardo2 > dardo3):
    dardo_vencedor = "Dardo 2"
elif (dardo1 == dardo2) and (dardo1 == dardo3):
    dardo_vencedor = "Empate"
else:
    dardo_vencedor = "Dardo 3"

# Saída de dados
if st.button("Apresentar dados de lançamento"):
    st.success(f"O dardo com a maior distância é {dardo_vencedor} com {maior_distancia}")

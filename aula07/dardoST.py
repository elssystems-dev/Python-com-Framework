import streamlit as st

def grafico(dardo1, dardo2, dardo3):
    # Apresentação de gráfico exibindo lançamento
    st.area_chart([0, dardo1], 
                use_container_width=True,
                height=200,
                color="#eaff00")
    st.area_chart([0, dardo2], 
                use_container_width=True,
                height=200,
                color="#ffa600")
    st.area_chart([0, dardo3], 
                use_container_width=True,
                height=200,
                color="#235fc7")

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
if (dardo1 == maior_distancia) and (dardo1 != dardo2) and (dardo1 != dardo3):
    dardo_vencedor = "1º dardo"
elif (dardo2 == maior_distancia) and (dardo2 != dardo1) and (dardo2 != dardo3):
    dardo_vencedor = "2º dardo"
elif (dardo3 == maior_distancia) and (dardo3 != dardo1) and (dardo3 != dardo2):
    dardo_vencedor = "3º dardo"
else:
    dardo_vencedor = "Empate"

# Saída de dados
if st.button("Apresentar dados de lançamento"):
    if dardo_vencedor == "Empate":
        st.warning("Houve um empate sem vencedores.")
        st.write(f"As distâncias máximas foram: {maior_distancia}")
    else:
        st.success(f"O dardo com a maior distância é {dardo_vencedor} com {maior_distancia}")
        grafico(dardo1, dardo2, dardo3)
        st.balloons()

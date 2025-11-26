import streamlit as st
# Esse código não funciona como deveria devido ao comportamento padrão do streamlit

listaNomes = []
listaIdades = []
listaAlturas = []
MenoresDezesseis = []

st.title("Pesquisa de navegação")

quantidadePessoas = int(st.number_input("Quantas pessoas serão registradas?", icon="❓", min_value=1, max_value=10))
vezes = quantidadePessoas

for i in range(vezes):
    st.header(f"{i+1}ª Pessoa: ")
    nome = st.text_input("Nome", icon="📝", placeholder="Digite o nome...", key=f"nome_{i+1}")
    idade = st.number_input("Idade", icon="🔢", placeholder="Digite a idade...", min_value=1, key=f"idade_{i+1}")
    altura = st.number_input("Altura (em metros)", icon="📏", placeholder="Digite a altura (em metros)...", min_value=0.01, max_value=2.80, key=f"altura_{i+1}")

    if st.button("Enviar", key=f"Button_{i+1}"):

        listaNomes.append(nome)
        listaIdades.append(idade)
        listaAlturas.append(altura)

        if listaIdades[i] < 16:
            MenoresDezesseis.append(nome)

        continue
    else:
        i = 0

if (i+1) == quantidadePessoas:
    st.subheader("Resultados")

    st.divider()

    st.text(f"A altura média dos participantes é de {sum(listaAlturas) / quantidadePessoas}")

    if MenoresDezesseis:
        st.text("Existem pessoas com menos de 16 anos nos dados inseridos.")
        st.text(f"E estes individuos são: {MenoresDezesseis}")
    else:
        st.text("Não existem menores de 16 anos nos dados inseridos.")
else:
    st.warning("Termine de adicionar os dados para ver os resultados.")
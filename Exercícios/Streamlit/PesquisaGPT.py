import streamlit as st

st.title("Pesquisa de navegação")

# Inicializar variáveis no estado da sessão
if "listaNomes" not in st.session_state:
    st.session_state.listaNomes = []
    st.session_state.listaIdades = []
    st.session_state.listaAlturas = []
    st.session_state.MenoresDezesseis = []
    st.session_state.indice = 0  # controla qual pessoa está sendo registrada

quantidadePessoas = st.number_input(
    "Quantas pessoas serão registradas?",
    min_value=1,
    max_value=10,
    step=1
)

i = st.session_state.indice

# Se ainda há pessoas a registrar:
if i < quantidadePessoas:
    st.header(f"{i + 1}ª Pessoa:")
    nome = st.text_input("Nome", key=f"nome_{i}", placeholder="Digite o nome...")
    idade = st.number_input("Idade", min_value=1, key=f"idade_{i}")
    altura = st.number_input("Altura (em metros)", min_value=0.01, max_value=2.80, key=f"altura_{i}")

    if st.button("Enviar", key=f"btn_{i}"):
        st.session_state.listaNomes.append(nome)
        st.session_state.listaIdades.append(idade)
        st.session_state.listaAlturas.append(altura)

        if idade < 16:
            st.session_state.MenoresDezesseis.append(nome)

        st.session_state.indice += 1  # avança para próxima pessoa
        st.rerun()
        # recarrega o app para atualizar o contador

else:
    # Mostrar resultados quando todas as pessoas forem registradas
    st.subheader("Resultados")
    st.divider()

    media_altura = sum(st.session_state.listaAlturas) / len(st.session_state.listaAlturas)
    st.text(f"A altura média dos participantes é de {media_altura:.2f} m")

    if st.session_state.MenoresDezesseis:
        st.text("Existem pessoas com menos de 16 anos nos dados inseridos:")
        st.text(", ".join(st.session_state.MenoresDezesseis))
    else:
        st.text("Não existem menores de 16 anos nos dados inseridos.")

    # Botão para reiniciar
    if st.button("Nova pesquisa"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()


import streamlit as st
import classes as cl

# Definição de <title> e <h1> da página
st.set_page_config("Idade x Salário")
st.title("Comparação de Idade e Salário")

# Definição de colunas

# Primeira coluna (Idade)
col1, col2 = st.columns([1, 1])
with col1:
    st.header("Função 1")
    st.divider() # <hr> do HTML para melhor visualização

    # Definindo formulário streamlit (Não reseta os dados sozinho)
    with st.form(key="Idade"):

        # Entrada de dados (Cada input com um valor chave diferente)
        st.text_input("Nome da pessoa um: ", icon="👤", key="nome1")
        st.number_input("Idade da pessoa um: ", icon="👶", min_value=1, key="idade1")   

        st.divider()

        st.text_input("Nome da pessoa dois: ", icon="👤", key="nome2")
        st.number_input("Idade da pessoa dois: ", icon="👶", min_value=1, key="idade2")

        # Definindo um botão submit (obrigatório em st.form())
        enviarIdade = st.form_submit_button("Enviar", key="IdadeFim")

        if enviarIdade:

            # As duas pessoas se transformam em um objeto cada na classe
            # st.session_state armazena o valor do input que possui a key referenciada

            pessoa1 = cl.Pessoa(st.session_state.nome1, st.session_state.idade1)
            pessoa2 = cl.Pessoa(st.session_state.nome2, st.session_state.idade2)

            # O parâmetro "self" da função eh_mais_velha representa a idade da própria pessoa
            # O outro parâmetro "idade" já puxa a idade do outro objeto que você quer referenciar.
            if pessoa1.eh_mais_velha(pessoa2.idade):
                st.write(f"{pessoa1.nome} é mais velha que {pessoa2.nome}")
            else:
                st.write(f"Pessoa um {pessoa2.nome}/ é mais velha que {pessoa1.nome}")

# Segunda coluna (Salário)
with col2:
    st.header("Função 2")
    st.divider()

    with st.form(key="Salario"):
        nomeUm = st.text_input("Nome da pessoa um: ", icon="👤", key="SLnome1")
        salarioUm = st.number_input("Salário da pessoa um (R$): ", icon="💵", min_value=1500.0, key="salario1")

        st.divider()

        nomeDois = st.text_input("Nome da pessoa dois: ", icon="👤", key="SLnome2")
        salarioDois = st.number_input("Salário da pessoa dois (R$): ", icon="💵", min_value=1500.0, key="salario2")

        enviarSalario = st.form_submit_button("Enviar", key="SalarioFim")

        if enviarSalario:
            funcionario1 = cl.Funcionario(st.session_state.SLnome1, st.session_state.salario1)
            funcionario2 = cl.Funcionario(st.session_state.SLnome2, st.session_state.salario2)
            st.write(f"A média salarial entre as duas pessoas é de R${funcionario1.salario_medio(funcionario2.salario):.2f}")

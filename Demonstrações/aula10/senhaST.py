import streamlit as st
# Problema senha fixa
st.title("Sistema de login simples")
# Declaração de constantes
# Credenciais fixas
USUARIO = "Clodoaldo"
SENHA = "senha123"

# Entrada de dados
usuario_entrada = st.text_input("Nome usuário:", placeholder="Digite um usuário...").capitalize()
senha_entrada = st.text_input("Senha", type="password", placeholder="Digite sua senha...")

# Estrutura de controle em loop
botao = st.button("Logar")

# Teste de tentavivas
MAXIMO_TENTATIVAS = 3

if 'tentativas' not in st.session_state:
    st.session_state.tentativas = 0

if botao is True:
    if st.session_state.tentativas >= MAXIMO_TENTATIVAS:
        st.error("Maximo de tentativas atingido. Acesso bloqueado")
    else:
        # Usar o while para controlar as tentativas
        while st.session_state.tentativas < MAXIMO_TENTATIVAS:
            if usuario_entrada == USUARIO and senha_entrada == SENHA:
                st.success("Login bem-sucedido")
                st.session_state.tentativas = 0
                break
            else:
                st.session_state.tentativas += 1
                st.error(f"Credenciais invalidas. Tentativa {st.session_state.tentativas} de {MAXIMO_TENTATIVAS}")
                break
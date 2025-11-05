import streamlit as st

TITULO = "Classificação de Níveis de Glicose no Sangue"

st.title(TITULO)
st.set_page_config(page_title=TITULO)

st.markdown("""
| Nível de glicose | Classificação |
|------------------|---------------|
|    0-7           |  Hipoglicemia |
|    70-100        |  Normal       |
|    101-140       |  Pré-diabetes |
|    141+          |  Diabetes     |
""")

# Entrada de dados

glicose = st.number_input("Insira o nível de glicose no sangue (mg/Dl):", min_value=0, max_value=800)

if st.button("Classificar"):
    if glicose <= 70:
        st.write("Nível de glicose classificado como Hipoglicemia")
    elif glicose <= 100:
        st.write("Nível de glicose classificado como Normal")
        st.balloons()
    elif glicose <= 140:
        st.write("Nível de glicose classificado como Pré-Diabetes")
    else:
       st.write("Nível de glicose classificado como Diabetes")

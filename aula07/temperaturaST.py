import streamlit as st

# Funções de conversão de temperatura

def Celsius_Fahrenheit(temp):
    return (temp * 1.8) + 32

def Celsius_Kelvin(temp):
    return (temp + 273.15)

def Fahrenheit_Celsius(temp):
    return (temp - 32) / 1.8

def Fahrenheit_Kelvin(temp):
    return ((temp - 32) / 1.8) + 273.15

def Kelvin_Celsius(temp):
    return (temp - 273.15)

def Kelvin_Fahrenheit(temp):
    return ((temp - 273.15) * 1.8) + 32

# Problema temperatura
st.sidebar.title("Conversor de Temperatura")
st.title("Conversor de Temperatura 🌡️")
st.sidebar.markdown("Converte a temperatura entre Celsius, Fahrenheit e Kelvin")

celsius_selecionado = st.sidebar.checkbox("Celsius", key="temp_celsius")
fahrenheit_selecionado = st.sidebar.checkbox("Fahrenheit", key="temp_fahrenheit")
kelvin_selecionado = st.sidebar.checkbox("Kelvin", key="temp_kelvin")

# Entrada de dados
temp = st.number_input("Valor da temperatura", format="%.2f", step=1.0)

# Processamento de dados
if st.button("Converter", icon="🔄"):
    if celsius_selecionado:
        st.subheader("Conversão com Celsius")
        st.write(f"{temp}℃ em Fahrenheit: {Celsius_Fahrenheit(temp)}℉")
        st.write(f"{temp}℃ em Kelvin: {Celsius_Kelvin(temp)}K ")
    if fahrenheit_selecionado:
        if celsius_selecionado == True:
            st.divider()
        st.subheader("Conversão com Fahrenheit")
        st.write(f"{temp}℉ em Celsius: {Fahrenheit_Celsius(temp)}℃")
        st.write(f"{temp}℉ em Kelvin: {Fahrenheit_Kelvin(temp)}K ")
    if kelvin_selecionado:
        if celsius_selecionado == True or fahrenheit_selecionado == True:
            st.divider()
        if temp < 0:
            st.error("A temperatura em Kelvin não pode ser negativa.")
        else:
            st.subheader("Conversão com Kelvin")
            st.write(f"{temp:.0f}K em Celsius: {Kelvin_Celsius(temp)}℃")
            st.write(f"{temp:.0f}K em Fahrenheit: {Kelvin_Fahrenheit(temp)}℉")
    elif not (celsius_selecionado or fahrenheit_selecionado or kelvin_selecionado):
        st.warning("Selecione pelo menos uma unidade para conversão e clique em 'Converter'.")
    if celsius_selecionado or fahrenheit_selecionado or kelvin_selecionado:
        st.snow()
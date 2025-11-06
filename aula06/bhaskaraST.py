from streamlit import header, write, text_input, button, warning, success, error
from math import sqrt, pow

delta = "(esperando dados...)"

header('Calculadora de Bháskara')
write("alculadora de raízes \n de uma equação de segundo grau")
write("ax² + bx + c = 0")


# Entrada de dados
a = text_input('Digite o valor de a:')
b = text_input('Digite o valor de b:')
c = text_input('Digite o valor de c:')

# Processamento de dados
if button("Calcular raízes"):
    try:
        a = float(a)
        b= float(b)
        c = float(c)
        delta = pow(b, 2) - 4 * a * c
        if delta < 0:
            warning("A equação não possui raízes reais")
        elif delta == 0:
            raiz = round((-b + sqrt(delta)) / (2*a), ndigits=3)
            success(f"A equação possui uma raíz real: {raiz}")
        else:
            raiz1 = round((-b + sqrt(delta)) / (2*a), ndigits=3)
            raiz2 = round((-b - sqrt(delta)) / (2*a), ndigits=3)
            success(f"As raízes da equação são:\n Raiz 1: {raiz1} \n Raiz 2: {raiz2} ")
    except:
        error("Por favor, insira valores válidos para a, b e c.")

write("O valor de delta é ", delta)

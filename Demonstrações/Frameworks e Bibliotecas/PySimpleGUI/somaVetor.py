import PySimpleGUI as sg
import numpy as np

# Lista para guarda o layout da janela
n = 0

layout = [
    [sg.Text("Digite a quantidade de números que deseja inserir: ")],
    [sg.Input(key='N')],
    [sg.Button("Ok"), sg.Button("Cancelar")]
]

janela = sg.Window("Calculadora", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or "Cancelar" in evento:
        janela.close()
        break
    elif evento == "Ok":
        try:
            n = int(valores['N'])
            if n <= 0:
                sg.popup("Insira somente números positivos")
                continue
            break
        except:
            sg.popup("Por favor, insira um valor válido")

janela.close()
numeros = [] # Outra lista

for i in range(n):

    layout = [
        [sg.Text(f"Digite o {i+1}º número")],
        [sg.Input(key='Campeão')],
        [sg.Button("Ok"), sg.Button("Cancelar")]
    ]

    janela = sg.Window("Entrada de número", layout)

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or "Cancelar" in eventos:
            janela.close()
            break
        elif eventos == "Ok":
            try:
                num = float(valores['Campeão'])
                numeros.append(num)
                break
            except ValueError:
                sg.popup("Por favor, insira valores válidos")

    if eventos == "Cancelar":
        break

janela.close() # Comando para fechar a janela
# Utilização do numpy
vetor = np.array(numeros)
# soma = np.sum(np.array(numeros))
soma = np.sum(vetor)
#media = np.mean(np.array(numeros))
media = np.mean(vetor)

# Resultados
resultado_layout = [
    [sg.Text("Elementos do vetor")],
    [sg.Text(",".join(map(str,vetor)))], 
    [sg.Text(f"Soma dos elementos = {soma}")],
    [sg.Text(f"Media dos elementos = {media}")],
    [sg.Button("Fechar")]
]

resultado_layout = sg.Window("Resultado", resultado_layout)

while True:
    eventoResultado = resultado_layout.read()
    if eventoResultado == sg.WINDOW_CLOSED or "Fechar" in eventoResultado:
        resultado_layout.close()
        break
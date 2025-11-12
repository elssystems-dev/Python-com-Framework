import PySimpleGUI as sg
import numpy as np

# Lista para guarda o layout da janela
layout = [
    [sg.Text("Digite a quantidade de números que deseja inserir: ")],
    [sg.Input()],
    [sg.Button("Ok"), sg.Button("Cancelar")]
]

sg.Window("Calculadora", layout).read()
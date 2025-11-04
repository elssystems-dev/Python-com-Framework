#---------------- Problema terreno ----------------

# Declaração de variáveis
largura:float
comprimento:float

# Entrada de Dados
largura = float(input("Digite a largura do terreno em metros:\n"))
comprimento = float(input("Digite a comprimento do terreno em metros:\n"))
valor_metro_quadrado = float(input("Digite o valor do metro quadrado do terreno em R$: "))

# Processamento de Dados
area = (largura * comprimento)
preco = area * valor_metro_quadrado

# Saída de Dados
print(f"A área do terreno é {area}M²")
print(f"O preço do terreno é de {preco:.2f} reais")
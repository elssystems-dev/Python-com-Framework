import os
os.system('cls')

# Zercício 1 - Atividade 01 (Sequencial)

preco_produto = float(input("Insira o preço unitário do produto:\n"))
quantidade = int(input("Digite a quantidade de produtos comprados:\n"))
dinheiro_cliente = float(input("Insira o valor em R$ recebido pelo cliente:\n"))

if preco_produto < 0 or quantidade < 0 or dinheiro_cliente < 0:
    if preco_produto < 0:
        print("\nO preço do produto está digitado em um valor negativo;")
    if quantidade < 0:
        print("A quantidade do produto está digitada em um valor negativo;")
    if dinheiro_cliente < 0:
        print("O dinheiro do cliente está digitado como negativo. Por acaso ele está devendo?;\n")
    print("Dito isso, reinicie o programa e digite os valores todos como positivos dessa vez.\n")
    quit()

valor_a_pagar = preco_produto * quantidade
troco = (dinheiro_cliente - valor_a_pagar)

if valor_a_pagar > dinheiro_cliente:
    print("O cliente está devendo!")
elif valor_a_pagar == dinheiro_cliente:
    print("Não haverá troco! O dinheiro do cliente cobre o total a ser pago!")
else:
    print(f"O troco será {troco:.2f}. ")

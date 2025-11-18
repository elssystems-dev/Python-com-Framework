import produtoOOP as p

# Entrada de dados
print("Entre com os dados do produto: ")

nome = input("Nome: ")
preco = float(input("Preço: R$").replace(",", "."))
saldo = int(input("Quantidade: "))

# Instanciar o meu projeto

ps = p.Produto(nome, preco, saldo)

# Saída de dados
print(ps.dadosDoProduto())
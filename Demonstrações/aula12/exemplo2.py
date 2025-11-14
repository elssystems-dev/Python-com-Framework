import produtoOOP as p # Importar o módulo

p1 = p.Produto() # Instanciar o objeto

# Entrada de dados
print("\nDigite os dados do produto")
p1.nome = input("\tNome: ")
p1.preco = float(input("\tPreço: R$ "))
p1.quantidade = int(input("\tQuantidade: "))

# Saída de dados 1
print("\nDados do produto")
print(f"\tNome do produto: {p1.nome}")
print(f"\tValor de compra: {p1.preco}")
print(f"\tQuantidade em estoque: {p1.quantidade}")
print(f"Valor total em estoque: R$ {p1.valorTotalEmEstoque():.2f}\n")

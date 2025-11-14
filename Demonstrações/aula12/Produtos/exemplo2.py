import produtoOOP as p # Importar o módulo

 # Instanciar o objeto
p1 = p.Produto()

# Entrada de dados
print("\nDigite os dados do produto")
p1.nome = input("\tNome: ")
p1.preco = float(input("\tPreço: R$ "))
p1.quantidade = int(input("\tQuantidade: "))

# Saída de dados 1
print(p1.dadosDoProduto())

#Adicionar produtos
q = int(input("Digite o número de produtos a ser adicionado pelo estoque: "))
p1.adicionarProdutos(q)

# Saída de dados 2
print("----- Dados atualizados -----")
print(p1.dadosDoProduto())

# Remover produtos
q = int(input("Digite o número de produtos a ser removido pelo estoque: "))
p1.removerProdutos(q)

# Saída de dados 3
print("--Dados atualizado--")
print(p1.dadosDoProduto())
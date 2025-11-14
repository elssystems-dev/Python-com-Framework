class Produto:

    # Atributos
    nome:str
    preco:float
    quantidade:int

    # self.quantidade é a quantidade atual, enquanto somente quantidade é o nome do parâmetro

    # Métodos
    def valorTotalEmEstoque(self) -> float:
        return (self.preco * self.quantidade)
    
    def adicionarProdutos(self, quantidade) -> int:
        self.quantidade += quantidade
        return self.quantidade
    
    def removerProdutos(self, quantidade) -> int:
        self.quantidade -= quantidade
        return self.quantidade

    def dadosDoProduto(self) -> str:
        saida = f'''
                Dados do produto: 
                \tNome do produto: {self.nome}
                \tValor de compra do produto: R$ {self.preco}
                \tQuantidade em estoque: {self.quantidade}
                \tValor total em estoque: R$ {self.valorTotalEmEstoque():.2f}
                '''
        return saida

        

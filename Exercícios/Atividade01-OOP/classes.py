class Pessoa:
    nome:str
    idade:int

    def __init__(self, nome:str = "", idade:int = 0):
        self.nome = nome
        self.idade = idade

    def eh_mais_velha(self, idade) -> bool:
        return self.idade > idade
    

class Funcionario:
    nome:str
    salario:float

    def __init__(self, nome:str = "", salario:float = 0.0):
        self.nome = nome
        self.salario = salario

    def salario_medio(self, outro_salario) -> float:
        return (self.salario + outro_salario) / 2
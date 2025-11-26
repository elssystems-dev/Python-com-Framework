class Contribuinte:
    __nome:str
    __rendaAtual:float

    @property
    def _nome(self) -> str:
        return self.__nome
    @_nome.setter
    def _nome(self, nome) -> str:
        if nome == "" or nome == None:
            raise ValueError("Valor inválido")
        else:
            self.__nome = nome
    
    @property
    def _rendaAtual(self) -> float:
        return self.__rendaAtual
    @_rendaAtual.setter
    def _rendaAtual(self, _rendaAtual) -> float:
        if _rendaAtual < 0 or _rendaAtual == None:
            raise ValueError("Valor inválido")
        elif _rendaAtual < 3.036:
            raise ValueError("Isenção de Valor (Digite R$3.036 ou acima)")
        else:
            self.__rendaAtual = _rendaAtual

    def __init__(self, nome:str, rendaAtual:float):
        self._nome = nome
        self._rendaAtual = rendaAtual

class Fisico(Contribuinte):
    __gastosSaude:float

    @property
    def _gastosSaude(self) -> float:
        return self.__gastosSaude
    @_gastosSaude.setter
    def _gastosSaude(self, gastosSaude) -> float:
        if gastosSaude < 0 or gastosSaude == None:
            raise ValueError("Valor inválido")
        else:
            self.__gastosSaude = gastosSaude

    def __init__(self, nome:str, rendaAtual:float, gastosSaude:float):
        super().__init__(nome, rendaAtual)
        self._gastosSaude = gastosSaude
        
    def definicaoImposto(self, rendaAtual, gastosSaude) -> float:
        if rendaAtual < 20000.00:
            imposto = (rendaAtual * 0.15) - rendaAtual
        else:
            imposto = (rendaAtual * 0.25) - rendaAtual
        
        if gastosSaude > 0:
            imposto += (gastosSaude * 0.5)
        return(f"Imposto a pagar: R${imposto:.2f}")

class Juridico(Contribuinte):
    __numeroFuncionarios:int

    @property
    def _numeroFuncionarios(self):
        return self.__numeroFuncionarios
    @_numeroFuncionarios.setter
    def _numeroFuncionarios(self, numeroFuncionarios):
        if numeroFuncionarios < 0 or numeroFuncionarios == None:
            raise ValueError("Valor inválido")
        else:
            self.__numeroFuncionarios = numeroFuncionarios

    def __init__(self, nome:str, rendaAtual:float, numeroFuncionarios):
        super().__init__(nome, rendaAtual)
        self._numeroFuncionarios = numeroFuncionarios
    
    def definicaoImposto(self, rendaAtual, numeroFuncionarios):
        if numeroFuncionarios > 10:
            imposto = (rendaAtual * 0.14) - rendaAtual
        else:
            imposto = (rendaAtual * 0.16) - rendaAtual
        return(f"Imposto a pagar: R${imposto:.2f}")
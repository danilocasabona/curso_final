from desafio.banco import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, agencia):
        super().__init__(nome, endereco)
        self.agencia = agencia
# 1. Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
# No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
from abc import ABC, abstractclassmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractclassmethod
    def ligar(self):
        pass

# 2. Crie uma nova classe chamada Carro que herda da classe Veiculo.
        
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        # 3. No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
        super().__init__(marca, modelo)
        self.cor = cor

    def ligar(self):
        print("Ligando o carro...")

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}"


# Em um arquivo chamado main2.py, importe a classe Carro.
# No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
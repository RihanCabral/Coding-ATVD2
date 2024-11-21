# Parte 2 Abstração

# Utilizando o módulo ABC para implementar a classe abstrata.
from abc import ABC, abstractmethod

# Criei uma classe abstrata Veiculo com os seguintes métodos abstratos:
class Veiculo(ABC):
    def __init__(self, marca, modelo):
        # Atributos da classe
        self.__marca = marca
        self.__modelo = modelo
        #  (iniciada em 0)
        self._velocidade = 0

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    # métodos abstratos não implementados na classer Veiculo:
    @abstractmethod
    def mostrar_velocidade(self):
        pass

    # métodos abstratos não implementados na classer Veiculo:
    @abstractmethod
    def acelerar(self):
        pass

    # métodos abstratos não implementados na classer Veiculo:
    @abstractmethod
    def freiar(self):
        pass
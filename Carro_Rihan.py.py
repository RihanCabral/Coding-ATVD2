# Parte 3 Herança
# Criando duas classes que herdam de Veiculo, Carro e Moto

from Veiculo import Veiculo
from Motor import Motor

class Carro(Veiculo):
    # Modificando a classe Carro para que tenha um atributo motor que é uma instância de Motor
    def __init__(self, marca, modelo, motor: Motor):
        super().__init__(marca, modelo)
        # Atributo do tipo Motor
        self.__motor = motor

    # Implementação do método abstrato:
    # Acelerar aumenta a velocidade em 80 km/h para Carro
    def acelerar(self):
        self._velocidade += 80

    # Implementação do método abstrato:
    # Frear reduz a velocidade em 35 km/h, não permitindo valores negativos
    def freiar(self):
        self._velocidade -= 35
        if self._velocidade < 0:
            self._velocidade = 0

    # Implementação do método abstrato:
    def mostrar_velocidade(self):
        return self._velocidade

    # Adicionar um método na classe Carro que exiba a potência do motor
    def getMotor(self):
        return self.__motor.getPotencia()

    def setMotor(self, motor):
        self.__motor = motor
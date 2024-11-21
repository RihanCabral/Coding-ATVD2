# Parte 3 Herança
# Criando duas classes que herdam de Veiculo, Carro e Moto

from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    # Implementação do método abstrato:
    # Acelerar aumenta a velocidade em 50 km/h para Moto
    def acelerar(self):
        self._velocidade += 50

    # Implementação do método abstrato:
    # Frear reduz a velocidade em 50 km/h, não permitindo valores negativos
    def freiar(self):
        self._velocidade -= 50
        if self._velocidade < 0:
            self._velocidade = 0

    # Implementação do método abstrato:
    def mostrar_velocidade(self):
        return self._velocidade

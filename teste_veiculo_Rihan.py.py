# Parte 4 Polimorfismo
from Carro import Carro
from Moto import Moto
from Motor import Motor

print('Testando as classes Carro e Moto herdadas de Veiculo e a composicao com a classe Motor:\n')

# Criação da função teste_veiculo(veiculo):
def teste_veiculo(veiculo):
    # Chamar acelerar() duas vezes:
    veiculo.acelerar()
    veiculo.acelerar()
    # Chamar mostrar_velocidade():
    print(f'Velocidade atual: {veiculo.mostrar_velocidade()} Km/h')
    # Chamar frear() uma vez:
    veiculo.freiar()
    # Chamar mostrar_velocidade() novamente:
    print(f'Velocidade atual: {veiculo.mostrar_velocidade()} Km/h\n')

# Testando essa função com instâncias de Carro e Moto.

# Inicializando o Motor dentro do construtor de Carro
carro = Carro('Honda', 'Civic', Motor(2.0))
# Mostrando como acessar atributos da classe composta
print(f'Dados do Carro: {carro.getMarca()} - {carro.getModelo()} - {carro.getMotor()}')
teste_veiculo(carro)

moto = Moto('Royal Enfield', 'Hunter 350')
print(f'Dados da Moto: {moto.getMarca()} - {moto.getModelo()}')
teste_veiculo(moto)
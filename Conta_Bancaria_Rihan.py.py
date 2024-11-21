# Parte 1: Encapsulamento
class ContaBancaria:
    
    #Classe que representa uma conta bancária com encapsulamento para proteger os dados.
    
    def __init__(self, numero_conta, titular, saldo_inicial=0):
        
        #Inicializa os atributos da classe com valores fornecidos e define saldo como privado.
        
        self._numero_conta = numero_conta
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, valor):
        
        #Adiciona o valor informado ao saldo da conta. 
        
        if valor > 0:
            self._saldo += valor
            return True
        return False

    def sacar(self, valor):
        
        #Subtrai o valor informado do saldo da conta, se houver saldo suficiente. 
        
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            return True
        return False

    def consultar_saldo(self):
        
        #Retorna o saldo atual da conta.
        
        return self._saldo

# Testes para a classe ContaBancaria
def testes_conta_bancaria():
    
#Executa testes básicos para verificar o funcionamento da classe ContaBancaria.
    
    #Criando uma conta bancária
    conta = ContaBancaria(numero_conta="12345", titular="João", saldo_inicial=1000)
    
    #Teste de depósito
    assert conta.depositar(500) == True, "Depósito falhou!"
    assert conta.consultar_saldo() == 1500, "Saldo incorreto após depósito!"

    #Teste de saque bem-sucedido
    assert conta.sacar(300) == True, "Saque válido falhou!"
    assert conta.consultar_saldo() == 1200, "Saldo incorreto após saque!"

    #Teste de saque maior que o saldo
    assert conta.sacar(1500) == False, "Saque inválido foi permitido!"
    assert conta.consultar_saldo() == 1200, "Saldo alterado indevidamente após tentativa de saque inválido!"

    #Teste de consulta de saldo
    assert conta.consultar_saldo() == 1200, "Consulta de saldo falhou!"

    print("Todos os testes passaram com sucesso!")
    
# Executar os testes
testes_conta_bancaria()

#Explicação do Pilar: Encapsulamento. 
""" 
    Os atributos privados (_numero_conta, _titular, _saldo) não são acessíveis diretamente.
    Apenas os métodos públicos (depositar, sacar, consultar_saldo) fornecem acesso controlado, garantindo que o saldo seja manipulado de forma segura e consistente.
"""
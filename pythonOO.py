# Programação Orientada a Objetos (POO):
class Conta:
    # Atributos da classe:
    codigos_bancos = {'Itáu': '1001', 'BB': '1002', 'Caixa': '1003'}

    def __init__(self, numero, titular, saldo, limite=1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        # self.__codigo_banco = '001'

    def extrato(self):
        print(
            "O saldo do titular {} é {}"
            .format(self.__titular, self.__saldo)
        )

    def __pode_sacar(self, valor_a_sacar):
        valor_maximo_pode_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_maximo_pode_sacar

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print('O valor {} ultrapassou o limite'.format(valor))

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, conta_recebidor):
        self.sacar(valor)
        conta_recebidor.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular.title()

    @property
    def numero(self):
        return self.__numero

    # Outra forma de fazer getter e setter
    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'


conta = Conta(1, 'anderson', 2000000)
conta2 = Conta(2, 'Guilherme', 1000000000)

print(Conta.codigo_banco())
print(Conta.codigos_bancos)

# conta.transferir(20000, conta2)
# conta2.extrato()
# conta.titular = 'bruno'
# print(conta.titular)
# conta.sacar(200000000)
# conta.extrato()

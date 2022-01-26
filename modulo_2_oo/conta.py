

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('construtor object... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = '001'
        self.__tarifa_transferencia = 8.0

    def extrato(self):
        print('Saldo de {} do titular {}.'.format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __podeSacar(self, valor):
        return valor <= (self.__saldo + self.__limite)

    def sacar(self, valor):
        if(self.__podeSacar(valor)):
            self.__saldo -= valor
            print("Saque efetuado.")
        else:
            print("Saldo insuficiente.")
            print('O valor {} passou o limite'.format(valor))

    def transferir(self, valor, destino):
        valorTotal = valor + self.__tarifaTransferencia

        if valorTotal < (self.__saldo + self.__limite):
            self.__saldo -= valorTotal
            destino.deposita(valor)

            print("Transferência efetuada.")
        else:
            print("Saldo insuficiente.")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'bb': '001', 'caixa': '002', 'nu': '042'}

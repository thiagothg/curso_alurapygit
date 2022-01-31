
class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0


    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return '>> Codigo {} - Saldo {} <<'.format(self.codigo, self.saldo)

conta = ContaCorrente(15)
conta.deposita(222)
print(conta)

conta2 = ContaCorrente(111)
conta2.deposita(122)
print(conta2)

contas = [conta, conta2]
contas_tuplas = (conta, conta2)
print(contas)
print(contas_tuplas)



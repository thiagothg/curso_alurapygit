from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def __str__(self):
        return '>> Codigo {} - Saldo {} <<'.format(self.codigo, self.saldo)

    def __eq__(self, other):
        return self.codigo == other.codigo

    def deposita(self, valor):
        self.saldo += valor

    @abstractmethod
    def passa_mes(self):
        pass


class ContaCorrente(Conta):

    def passa_mes(self):
        self.saldo -= 2


class ContaPoupanca(Conta):
    def passa_mes(self):
        self.saldo *= 1.01
        self.saldo -= 3


class ContaInvestimento(Conta):
    def passa_mes(self):
        pass


class ContaSalario:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def __str__(self):
        return '>> Codigo {} - Saldo {} <<'.format(self.codigo, self.saldo)

    def __eq__(self, other):
        return self.codigo == other.codigo

    def deposita(self, valor):
        self.saldo += valor


conta = ContaCorrente(200)
conta.deposita(1000)
conta.passa_mes()

conta_po = ContaPoupanca(200)
conta_po.deposita(1000)
conta_po.passa_mes()

investimento = ContaInvestimento(22)
investimento.passa_mes()

contas = [conta, conta_po, investimento]
print(conta == conta_po)
for c in contas:
    c.passa_mes()
    print(c)

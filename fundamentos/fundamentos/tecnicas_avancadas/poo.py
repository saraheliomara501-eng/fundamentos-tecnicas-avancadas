class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def get_saldo(self):
        return self.__saldo

conta = ContaBancaria(100)
conta.depositar(50)
print(conta.get_saldo())

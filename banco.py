class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito realizado. Novo saldo: {self.saldo}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque realizado. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente para saque.")

    def extrato(self):
        print(f"Saldo atual: {self.saldo}")


class ContaBancária:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        if valor >0:
           self.__saldo=  self.__saldo + valor
           print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor >0 and valor <= self.__saldo:
            self.saldo = self.saldo - valor
            print(f"Saque de R$ {valor:.2f} realizado.")
        elif valor <= 0:
            print("Valor de saque inválido.")
        else:
            print("Saldo insuficiente para realizar o saque.")
    def get_saldo(self):
        return self.__saldo
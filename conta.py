

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.numero = 123
        self.titular = "Nico"
        self.saldo = 55.0
        self.limite = 1000.0

    def extrato(self):
        print("Saldo de {} do titular {}" .format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
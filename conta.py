class Conta:
    def __init__(self, numero, correntista, saldo):
        self.numero = numero
        self.correntista = correntista
        self.saldo = saldo

    # Getters
    def get_numero(self, numero):
        return self.numero

    def get_correntista(self, correntista):
        return self.correntista

    def get_saldo(self, saldo):
        return self.saldo

    # Setters
    def set_numero(self, numero):
        self.numero = numero

    def set_correntista(self, correntista):
        self.correntista = correntista

    def set_saldo(self, saldo):
        self.saldo = saldo

    # Métodos
    def imprimir(self):
        print("Conta Nº: ", self.numero, " Correntista: ", self.correntista, " Saldo em conta: ", self.saldo)

    def deposita(self):
        deposito = float(input("Informe o valor do depósito: "))
        self.saldo += deposito
        print("Saldo atual: ", self.saldo)

    def saca(self):
        saque = float(input("Informe o valor do saque: "))
        if self.saldo >= saque:
            self.saldo -= saque
            print("Saldo atual: ", self.saldo)
        else:
            print("Sem limite para realizar o saque.")
            print("Saldo atual: ", self.saldo)

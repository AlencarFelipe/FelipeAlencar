class Banco:
    def __init__(self, nome , conta , agencia):
        self.nome = nome
        self.conta = conta
        self.agencia = agencia

def pagamento(conta, agencia, saldo, valor_aluguel):
    # conta= int(input("Digite o numero da sua conta"))
    # agencia= int(input("Digite o numero da sua agencia"))
     if saldo >= valor_aluguel:
      return saldo - valor_aluguel
     else:
         print("Saldo insuficiente")

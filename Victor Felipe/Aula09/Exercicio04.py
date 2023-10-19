#crie uma classe pedido que permite criar objetos que representem pedidos em um restaurante. Cada objeto de pedido deve conter informaç~es como onome do cliente , itens do pedido e o valor total
class Pedido:

    def __init__(self, nome, produto, valor_total):
        self.nome = nome
        self.produto = produto
        self.valor = valor_total
 
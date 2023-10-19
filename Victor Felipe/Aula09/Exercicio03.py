#Criar uma classe pessoa que possui um atributo de classe para manter o numero de pessoas criadas. cada vez que voc~e instancia um objeto da classe pessoa, o 
class Pessoa:
    total_pessoas = 0 #Atributo

    def __init__(self, nome, idade,):
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas +=1


pessoa1 = Pessoa("Felipe")
pessoa2 = Pessoa("Victor")

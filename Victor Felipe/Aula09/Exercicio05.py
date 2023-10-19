#crie uma classe tarefa que representa uma tarefa a ser realizada. A calsse deve ter atributos como nome da tarefa, data de vencimento e status ( pendente , em andamento , concluido. Implemente metodos para marcar a tarefa
class Tarefa:
    def __init__(self, nome_tarefa, data_venci, ):
         self.nome_tarefa = nome_tarefa
         self.data_venci = data_venci
         self.status = "Pendente"

    def tarefa_concluida(self):
         self.status == "Concluida"

    def data_verificar(self):
         data_tarefa = input("Digite uma data :")
         if self.status == "pendente" and data_tarefa > self.data_venci:
           return f"A tarefa {self.nome_tarefa} esta atrasada"
         
         else:
          return f"A tarefa {self.nome_tarefa} esta em andamento"
         

tarefa1 = Tarefa ("Passear com o cahorro " , "2023-10-1/")
print (tarefa1.data_venci())
print (tarefa1.status())                  
        


#crie uma classe aluno que possuiatributos como nome , idade e notas. implemnet emetodos para calcular a media das notas e verificar se o aluno foi aprovado (media maior ou igual a 6)
class Aluno:
   def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

      

   def calcular_media(self, nota,):
     return nota / 3
   
   def aprovação_reprovação(self, nome , nota):
      if (nota >= 6):
         return f"{self.nome} foi aprovado"
      else:
         return f"{self.nome} foi reprovado"
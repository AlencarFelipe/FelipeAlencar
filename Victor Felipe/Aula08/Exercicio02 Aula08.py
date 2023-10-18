"""class Automovel:
  def __init__(self, modelo, marca, cor):
      self.modelo = modelo
      self.marca = marca
      self.cor = cor
  def acelerar():
      return print ("Vrummm")


automovel_1 = Automovel("lancer","mitisibushi","Prata")
automovel_1.acelerar()"""

class Retangulo:
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self, base, altura):
        base = int(input("Digite a base: "))
        altura = int(input("Digite a altura: "))
        print (f"A area do retangulo é: {base * altura}")

retangulo_1 = Retangulo(15,2)

retangulo_1.calcular_area(15,2)

print(retangulo_1)


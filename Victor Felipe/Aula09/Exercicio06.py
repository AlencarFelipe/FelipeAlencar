#Criar calculadora interativa com classe calculdora
from Exercicio01 import Calculadora
calculadora = Calculadora()
print("*********************************************")
print("Bem Vindo a caluculadora Python")


while(True):
    print("Escolha uma opção \n")
    print("Opção 1: Adição \n")
    print("Opção 2: Subtração \n")
    print("Opção 3: Multiplicação \n")
    print("Opção 4: Divisão \n")
    print("Opção 5: Sair \n")

    opcao = int(input())
    if (opcao == 5):
        print("Você saiu...")
        break

    a = int(input("Digite o primeiro numero: "))
    b = int(input("Digite o segundo numero: "))
    
 

    if (opcao == 1):

        print("O resultado da soma é: " , calculadora.somar(a,b))

    elif (opcao == 2):
       print("O resultado da subtração é: ", calculadora.subtrair(a,b))


    elif (opcao == 3): 
      print("O resultado da multiplicação é: ", calculadora.multiplicar(a,b))


    elif (opcao == 4):
        print("O resultado da divisão é: " , calculadora.dividir(a,b))
        
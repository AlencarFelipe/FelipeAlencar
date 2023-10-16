""""def saudacao(nome, sobrenome):
    print(f"Miha saudacao ao... {nome} {sobrenome}")

"""
num1 = 0
num2 = 0
def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def dividir(num1, num2):
    return num1 // num2

def multiplicar(num1, num2):
    return num1 * num2

def menu():
       
       
    while True:
        print("Escolha uma opção \n")


        print("Opção 1: Adição \n")
        print("Opção 2: Subtração \n")
        print("Opção 3: Divisão \n")
        print("Opção 4: Multiplicação \n")
        print("Opção 5: Sair \n")
        
        opcao = int(input())

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
                        
        if  (opcao == 5):
                break

        elif (opcao == 1):
                
                    print(somar(num1, num2))

        elif (opcao == 2):
                
                   print(subtrair(num1, num2))

        elif (opcao == 3):
                
                     print(dividir(num1, num2))

        elif (opcao == 4):
                
                    print(multiplicar(num1, num2))


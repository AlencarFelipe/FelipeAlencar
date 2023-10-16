print("*********************************************")
print("Bem Vindo a caluculadora Python")

numero_1 = float(input("Digite o primeiro número"))
numero_2 = float(input("Digite o segundo número"))
while(True):
    print("Escolha uma opção \n")
    print("Opção 1: Adição \n")
    print("Opção 2: Subtração \n")
    print("Opção 3: Multiplicação \n")
    print("Opção 4: Divisão \n")
    print("Opção 5: Sair \n")

    opcao = int(input())
    
    if (opcao == 5):
        break

    elif (opcao == 1):
        adicao = numero_1 + numero_2
        print(numero_1)
        print(numero_2)
        print("O resultado da sua adição é : " , print(adicao))

    
    elif (opcao == 2):
        subtracao = numero_1 - numero_2
        print(numero_1)
        print(numero_2)
        print("O resultado da sua subtracao é : " , print(subtracao))

    elif (opcao == 3):
        multiplicacao = numero_1 * numero_2
        print(numero_1)
        print(numero_2)
        print("O resultado da sua multiplicacao é : " , print(multiplicacao))

    elif (opcao == 4):
        divisao = numero_1 // numero_2
        print(numero_1)
        print(numero_2)
        print("O resultado da sua divisao é : " , print(divisao))






        


  
            





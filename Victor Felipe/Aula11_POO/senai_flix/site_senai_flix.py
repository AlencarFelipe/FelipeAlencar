from filme import Filme, Serie, Documentario
from cliente import Cliente
from login import Login
from conta import Conta
from cadastro import Cadastro


print("**********************************************")
print("         Bem Vindo ao SenaiFlix               ")
print("**********************************************")






titulos = {}
while True:
    print("Escolha uma opção \n")
    print("Opção 1: Inserir Titulos \n")
    print("Opção 2  Listar Titulos  \n")
    print("Opção 3: Atualizar Titulos\n")
    print("Opção 4: Deletar Titulos\n")
    print("Opção 5: Sair \n")


  
    opcao = int(input("Digite a opção: \n"))

    if (opcao == 5):
        break

    elif opcao == 1:
        while True:
            print("Escolha uma opção \n")
            print("Opção 1: Inserir Filmes \n")
            print("Opção 2  Inserir Series  \n")
            print("Opção 3: Inserir Documentarios\n")
            print("Opção 4: Sair \n")

            opcao = ""

  
    opcao = input("")

    if opcao == 4:
        break


    elif opcao == 1:
        cliente01 = Cliente( nome = input("Digite seu nome: ", endereco = input ("Dgite seu endereço") , email = input ("Digite seu email")))

        







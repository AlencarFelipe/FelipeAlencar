from filme import Filme, Serie, Documentario
from cliente import Cliente
from login import Login

print("**********************************************")
print("         Bem Vindo ao SenaiFlix               ")
print("**********************************************")




login = Login()
login.efetua_login()



titulos = {}
while True:
    print("Escolha uma opção \n")
    print("Opção 1: Inserir Titulos \n")
    print("Opção 2  Listar Titulos  \n")
    print("Opção 3: Atualizar Titulos\n")
    print("Opção 4: Deletar Titulos\n")
    print("Opção 5: Sair \n")


  
    opcao = input("")

    if (opcao == "5"):
        break

    elif opcao == "1":
        while True:
            print("Escolha uma opção \n")
            print("Opção 1: Inserir Filmes \n")
            print("Opção 2  Inserir Series  \n")
            print("Opção 3: Inserir Documentarios\n")
            print("Opção 4: Sair \n")

            opcao = ""

  
    opcao = input("")

    if opcao == "4":
        break


    elif opcao == "1":
        filme = Filme("")








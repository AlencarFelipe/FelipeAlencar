#Crie uma função que peça para o usuario digitar o caminho de uma pasta/diretorio e que liste os arquivos de um diretorio utilizando a biblioteca OS

import os
def listar_arquivos():
    caminho_diretorio = input("Informe o caminho do diretorio")

# Listar os arquivos do diretorio passado
    arquivos = os.listdir(caminho_diretorio)
    print("Os Arquivos do diretorio passado são: ")

    for arquivo in arquivos:
        print(arquivo)

    else:
        print ("Diretorio invalido")

listar_arquivos()
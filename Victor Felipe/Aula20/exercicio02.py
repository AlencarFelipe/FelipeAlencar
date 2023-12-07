# Crie uma função que cria um diretorio e pergunta ao usuario aqual sera o nome
import os

def criar_diretorio():


    nome_diretorio = input("Denomeie o  seu novo diretorio :") 

# Criar um novo diretorio
    novo_diretorio = os.path.join(os.getcwd(), nome_diretorio)

# Criando um novo diretorio
    os.mkdir(novo_diretorio)

    print(f"Seu novo diretorio '{nome_diretorio}' foi criado com sucesso \n")

criar_diretorio()

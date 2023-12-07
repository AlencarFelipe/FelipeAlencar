import os

# Exemplo 1: Obter o Diretorio de trabalho Atual

diretorio_atual = os.getcwd()
print( f" O Diretorio atual é {diretorio_atual}")

# Analisar os arquivos em um diretorio

diretorio = "A:\\Prof. Cassio de Albuquerque\Python III\Victor Felipe"

arquivos = os.listdir(diretorio)

print("Os Arquivos do diretório são: ")
for arquivo in arquivos:
    if(arquivo == "teste_pyautoGUI"):
        print(arquivos)

    else:
        print("Arquivo não encontrado")



# Criar um diretorio

novo_diretorio = "A:\\prof. Cassio de Albuquerque\\Python III\Victor Felipe"

os.mkdir(novo_diretorio)

# Exemplo comandos no sistema
contador = 0
while contador < 18:
    os.system("echo Ola, mundo")
    contador == 1
#Echo sera usado para print no cwd
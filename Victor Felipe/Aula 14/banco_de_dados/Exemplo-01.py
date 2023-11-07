import mysql connector 

# Configuração da conexão com o banco de dados
config = {
 'user': 'se_usuario';
 'password' : 'sua_senha';
 'host': 'localhost'
 'database': 'nome_do_banco_de_dados'
}

#Estabelecer a conexão com o banco de dados
conexao = mysql.connector.connect(**config)

#criar um cursor para executar consultas SQL
cursor = conexao.cursor()

# Exemplo de consulta SQL
selecionarDB = "use loja_II"
consulta = "SELECT * FROM tabela"

# Executar a consulta
cursor.execute(consulta)

# Recuperar os resultados
resultados = cursor.fatall()

#Imprimir os resultados
for linha in resultados:
    print(linha)


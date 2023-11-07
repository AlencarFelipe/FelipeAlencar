import mysql.connector

config = {
 'user': 'root',
 'password' : 'senai',
 'host': 'localhost',
 'database': 'loja_ii'
}

#Estabelecer a conexão com o banco de dados
conexao = mysql.connector.connect(**config)

#criar um cursor para executar consultas SQL
cursor = conexao.cursor()

# Exemplo de consulta SQL
#selecionarDB = "use loja_II"
consulta = "INSERT INTO clientes('nome', 'endereco', 'e_mail') VALUES ('Ana Paula','rua do bosque', 'ana@ana.com')"

# Executar a consulta
#cursor.execute(selecionarDB)
cursor.execute(consulta)

# Recuperar os resultados
resultados = cursor.fetchall()

#Imprimir os resultados
for linha in resultados:
    print(linha)


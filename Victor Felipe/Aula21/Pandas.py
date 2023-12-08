import pandas as pd
import matplotlib.pyplot as plt

# Criar de  um Dataframe
# Dados ficticio

dados_alunos = {
    'Nome': ['Victor','Gabriel','Mariana', 'Sarah'],
    'Idade': [18,20,19,22],
    'Nota_Matematica': [90,85,88,92],
    'Nota_Portugues' : [69,80,99,70]
}

# Passo 2 : Criar o Dataframe
df_alunos = pd.DataFrame(dados_alunos)

# Passo 3 Exibir o data frame
print(df_alunos)

# Media das notas de Matemaica

media_matematica = df_alunos['Nota_Matematica'].mean()
media_portugues = df_alunos['Nota_Portugues'].mean()

# Imprimir a Media
print(f"Media em Matematica:{media_matematica}.")
print(f"Media em Portugues:{media_portugues}.")

##################################################

#Visualização de dados:

#Grafico de Barra das Notas de Matematica;

df_alunos.plot( x = 'Nome', y=['Nota_Matematica', 'Nota_Portugues'],
kind='line' )

plt.title("notas dos Alunos em Matemtaica e Portgues")

plt.xlabel("Aluno")
plt.ylabel("Nota")
plt.show()
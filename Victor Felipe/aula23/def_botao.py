import pandas as pd
import matplotlib.pyplot as plt

def gerar_grafico():
    dados_graficos = 'teclado.xlsx'

    # Passo 2: Ler os dados usando pandas
    dados = pd.read_excel(dados_graficos)

    ##################################################

    # Visualização de dados:

    # Gráfico de Barra das Notas de Matemática;
    dados.plot(x='Título', y=['Preço'], kind='bar')

    plt.title("Preço médio do Produto")
    plt.xlabel("Produto")
    plt.ylabel("Preço")
    plt.show()

# Chamar a função para gerar o gráfico
gerar_grafico()
import requests
from bs4 import BeautifulSoup

def pesquisa_produto():

# Solicita uma pesquisa para o usuario
    produto_pesquisa = input("Qual produto você está procurando: ")

# Substitui os espaços em branco por +
    produto_pesquisa = produto_pesquisa.replace(' ', '+')

# Atrela o Input na URL
    url = f'https://www.amazon.com.br/{produto_pesquisa}'

# Solicita uma resposta com a URl
    response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida (código status 200)
    if response.status_code == 200:

# Permiti a analise de forma eficiente do conteudo da pagina
        soup = BeautifulSoup(response.text, 'html.parser')

# Encontra produtos que tenha determinada classe
        resultados = soup.find_all('li', class_='ui-search-layout__item')

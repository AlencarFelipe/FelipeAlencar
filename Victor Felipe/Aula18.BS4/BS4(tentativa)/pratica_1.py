import requests
from bs4 import BeautifulSoup

def pesquisar_no_mercado_livre():
# Solicitar uma pesquisa
    produto_pesquisa = input("Qual produto você está procurando: ")
# Substituir os espacos por '+' para formatar coretamente a URL
    produto_pesquisa = produto_pesquisa.replace('', '+')

# URL de pesquisa do MErcado Livre

    url = f'https:///lista.mercadolivre.com.br/{produto_pesquisa}'

# Enviar uma solicitação GET para a pagina de pesquisa
    response = requests.get(url)

#Verificar se a solicitação foi bem sucedida (codigo status 200)
    if response.status_code == 200:
#Criar um objeto BeautifulSoup para analisar o conteudo da pagina de pesquisa
        soup = BeautifulSoup(response.text, 'html.parser')

# Exibir todos os elementos HTML correspondentes a pesquisa
        resultados = soup.find_all('li', class_='ul-search-layout_item')

# Exibi informações sobre os primeiros resultados
        for resultado in resultados[:5]:# Exibi os primeiros resultados

            nome_produto = resultado.find('h2', class_='ul-search-item_title').text
            preco_produto = resultado.find('h2', class_='price-tag-faction').text
            link_produto = resultado.find('a', class_='ul-search-link')['href']
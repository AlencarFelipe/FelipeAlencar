#Importar a biblicote BS4

from bs4 import BeautifulSoup
import requests

#URL da página web a ser raspada

url ='https://www.mercadolivre.com.br/cola-para-extenso-de-cilios-sobelle-power-full-3ml/p/MLB23138898?pdp_filters=item_id:MLB3356026281#is_advertising=true&searchVariation=MLB23138898&position=1&search_layout=grid&type=pad&tracking_id=bc2558c3-4757-4961-82a0-fe1340fb5d42&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=1&ad_click_id=MmYyNGQzOWEtYjFmOC00MjBlLWIyYzMtYWI3MTdiZmQxNWQz'

#Enviar uma solicitação GET para nossa página

response = requests.get(url)

#Verificar se solicitação foi bem sucedida

if response.status_code == 200:
    #Criar um objeto BeautifulSoup para analisar o nosso conteúdo html da página

    soup = BeautifulSoup(response.text, 'html.parser')
    # Procura o primeiro elemento h1
    h1 = soup.find('h1')
    #Exibir o texto dentro da tag h1
    print(f'Título da Página: {h1.text}')

    #Exibir todos os elementos HTML correspondentes a uma tag específica

    #Procura por todos os links na página
    todos_links = soup.find_all('a')

    #Exibir os URLS de todos os links na página
    for link in todos_links:
        print(link.get('href'))

    #Acessar atributos de um elemento HTML
    img_src = soup.find('img')['src']

    #Navegar pela arvore DOM, navegar pelo HTML para encontrar elementos aninhados

    conteudo_div = soup.find('div', class_='ui-pdp-header__title-container')
    conteudo_spam = soup.find('spam', class_='andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact')

    #Exibir o texto dentro da tag < div class='conteudo'>

    print('Conteudo da Div:')
    print(conteudo_div.text.strip())


    #Encontrar todos os elementos de uma classe específica

    todos_elementos_classe_x= soup.find_all(class_='ui-search-item__brand-discoverability ui-search-item__group__element')

    print(todos_elementos_classe_x.text.strip())


    #Econtrar o próximo elemento irmão

    elemento_filho = title_tag.find_next_sibling()


    #Econtrar elementos pelo seletor CSS
    elemento_css = soup.select('.minha-classe_css')

else:

    print(f"A solicitação falhou com o código de status {response.status_code}")

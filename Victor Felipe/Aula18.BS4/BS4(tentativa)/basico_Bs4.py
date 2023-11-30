#Importar a biblioetca BS4

from bs4 import BeautifulSoup
import requests

# URL da pagina web a ser raspada

url = 'https://www.mercadolivre.com.br/'

#Enviar uma solicitação GET para a pagina

response = requests.get(url)

#Verificar se a solicitação foi bem sucessidida

if response.status_code == 200:
#Criar um objeto BS para analisar o nosso conteudo html da pagina
    soup = BeautifulSoup(response.text, 'html.parser')

#Procura o primeiro elemento h1
    h1 = soup.find('h1')


#Exiibir o texto dentro da tag h1
    print(f'Titulo da pagina: {h1.text}')

# Exibir todos os elementos HTML correspondentes a uma tag especifica

# Procura por todos os links da pagina
    todos_links = soup.find_all('a')

# Exibir os URLs de todos os links da pagina
    for link in todos_links:
        print(link.get('href'))

    #Acessae atributos de um elemento HTML
    img_src = soup.find('img')['src']

    print(img_src)

    # Navegar pela arvore DOm, navegar pelo HTML para encontrar elementos

    conteudo_div = soup.find('div' ,class_='ui-pdp-title')
    print(conteudo_div)
    conteudo_spam = soup.find('spam', 'class_:')

    #Exibir o texto dentro da tag < div calss=' conteudo'>

    print('Conteudo da Div:')
    print(conteudo_div.text.strip())
    print('Preço do produto:')
    print(conteudo_spam.text.strip())

    # Encontar todos os elementos de ua classe especifica

    todos_elementos_classes_x = soup.find_all (class_= '')

    print(todos_elementos_classes_x.text.strip())

    # Encontar o proximo elemento irmao

    elemento_filho = title_tag.find_next_sibiling()

    # Encontar elementos pelo seletor CSS

    elemento_css = soup.select(' .minha-classe_css')

else:
    print(f"A solicitação falhou com o código")
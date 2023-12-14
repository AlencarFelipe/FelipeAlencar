"Entrada para usuario digitar o site, Entrada para palavra de pesquisa"

import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from operator import itemgetter

def entrar_navegador():
    lista_produtos = []
    
    # Inicializa o navegador
    navegador = webdriver.Chrome()
    navegador.get("https://www.mercadolivre.com.br/")
    sleep(2)

    # Pesquisa o produto
    pesquisa = entrada_txt.get()
    pesquisa_tv = navegador.find_element(By.ID, "cb1-edit")
    pesquisa_tv.send_keys(pesquisa)
    pesquisa_tv.submit()
    sleep(2)

    # Puxa as informações
    conteudo_pag = navegador.page_source
    site = BeautifulSoup(conteudo_pag, 'html.parser')

    flag_pagina_seguinte = True

    while flag_pagina_seguinte:
        produtos = site.findAll('div', attrs={'class': 'ui-search-result'})

        for produto in produtos:
            h_ref = produto.find('a')
            preco = produto.find('span', attrs={'aria-roledescription': 'Preço'}).contents[1].text
            preco = preco.replace('.', '')
            preco = preco.replace(',', '.')  # Trata os dados
            preco = float(preco)

            lista_produtos.append([h_ref['title'], "{:2f}".format(preco), h_ref['href'], preco])

        try:
            btn_seguinte = navegador.find_element(By.XPATH, value="//a@title=Seguinte']")
            navegador.execute_script("arguments[0].click();", btn_seguinte)
            sleep(5)

        except:
            flag_pagina_seguinte = False
            pass

    # Organiza os dados
    lista_ordenada = sorted(lista_produtos, key=itemgetter(3))

    # Remove a coluna temporária usada para ordenação
    for item in lista_ordenada:
        del item[3]

    # Cria o DataFrame e salva como um arquivo Excel
    arq_produtos = pd.DataFrame(lista_ordenada, columns=['Título', 'Preço', 'Link'])
    arq_produtos.to_excel(f'{pesquisa}.xlsx', index=False)

    print(lista_ordenada)

# Cria uma janela
janela = tk.Tk()

# Cria um Label - Produto
label = tk.Label(janela, text="produto")
label.pack()

# Criar uma área para inserir texto
entrada_txt = tk.Entry(janela, width=50)
entrada_txt.pack()

# Button: Botão:
botao_executar = tk.Button(janela, text="Executar", command=entrar_navegador)
botao_executar.pack()

def on_enter_press(event):
    if event.keysym == "Return":
        entrar_navegador()
janela.bind("<KeyPress>", on_enter_press)

#####################################################################################################################################


def gerar_grafico():
    dados_graficos = (f"{entrada_txt.get()}.xlsx")

    # Passo 2: Ler os dados usando pandas
    dados = pd.read_excel(dados_graficos)
    
    # Verifique se o arquivo Excel existe antes de tentar lê-lo
    if os.path.exists(dados_graficos):
        # Passo 2: Ler os dados usando pandas
        dados = pd.read_excel(dados_graficos)

        # Visualização de dados:
        # Gráfico de Barra das Notas de Matemática;
        dados.plot(x='Título', y=['Preço'], kind='bar')

        plt.title("Preço médio do Produto")
        plt.xlabel("Produto")
        plt.ylabel("Preço")
        plt.show()
    else:
        messagebox.showerror("Erro", f'O arquivo {dados_graficos} não foi encontrado.')



# Button: Botão:
botao_grafico = tk.Button(janela, text="Gráfico", command=gerar_grafico)
botao_grafico.pack()

janela.mainloop()
gerar_grafico()
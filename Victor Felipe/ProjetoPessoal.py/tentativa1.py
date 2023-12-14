# Importa as bibliotecas
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



#Instancia o navegador
navegador = webdriver.Edge()

#Digita e busca a URl
navegador.get("https://github.com/login")

try: #Encapsula o  cogido que pode gerrar erro
    time.sleep(2) #Aguarda 2 segundos

    #Enconta pelo ID
    elemento = navegador.find_element(By.ID,"login_field")

    #Digita email 
    elemento.send_keys("")

    #Enconta pelo ID
    elemento = navegador.find_element(By.ID,"password")

    #Digita senha
    elemento.send_keys("")


    #Confirmação do digitado
    elemento.send_keys(Keys.RETURN)
    time.sleep(3)
    

    # Encontra o elemento de salvar pela classe
    elemento = navegador.find_element(By.CLASS_NAME, "avatar-user")
    elemento.click()
    time.sleep(2)

    navegador.get("")
    time.sleep(3)


    elemento = navegador.find_element(By.ID, ":R2ekqjal5:")
    elemento.click()
    time.sleep(3)

    elemento = navegador.find_element(By.ID, ":r2l:--label")
    elemento.click()
    time.sleep(3)

    # navegador.get("https://github.com/AlencarFelipe/Felipe_Python_SENAI/upload/main/Victor%20Felipe")
    # time.sleep(3)


finally: #Fecha o navegador
    navegador.close


"""criar um scrip com selenium e pyautogui que pesquisa
sobre um tema no google, copia e cola o titulo no bloco de notas
e o salva.
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time


# Selenium
navegador = webdriver.Chrome()
navegador.get("https://www.google.com.br/")
time.sleep(3)

# PyautoGUI
pyautogui.write("The Boys 4 temporada")
pyautogui.press("enter")

elemento = navegador.find_element(By.ID,"APjFqb")
texto_elemento = elemento.text
time.sleep(3)



pyautogui.press('winleft')
programa = "Bloco de Notas"
pyautogui.write(programa)
pyautogui.press('enter')

pyautogui.write(texto_elemento)


time.sleep(3)
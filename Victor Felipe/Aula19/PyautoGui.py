import pyautogui
import time

# Aguardar alguns segundos antes de inicar
time.sleep(5)

# Obtenha a imprima as dimensões da tela
'''largura, altura = pyautogui.size()
print(f"A largura da tela é de: {largura}\n. A altura da tela é de: {altura}. ")

# Mover o mouse para as coordenadas (x,y) e clique
pyautogui.move(200, 200, duration=1)
pyautogui.click()

# Digite algo usando o teclado virtual
pyautogui.typewrite("Hello, World")'''

# Obter e imprimir a posição atual do mouse

while True:

    x,y = pyautogui.position()
    print(f"A posição atual do mouse é {x} and {y}. ")

#Exibir um alerta

pyautogui.alert("Isto é um aviso")

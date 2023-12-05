"""voce deve escrever uma automação com pythonautogui pela qual o 
programa abre o bloco de notas, e digita uma mensagem e o salva"""

import pyautogui
import time

pyautogui.press('winleft')
programa = "Bloco de Notas"
pyautogui.write(programa)
pyautogui.press('enter')

time.sleep(2)

pyautogui.typewrite("Hello, World")
time.sleep(2)

pyautogui.hotkey('ctrl', 's')
time.sleep(2)

nome_arquivo = 'hello.txt'
time.sleep(2)

pyautogui.typewrite(nome_arquivo)
time.sleep(2)

pyautogui.press("enter")


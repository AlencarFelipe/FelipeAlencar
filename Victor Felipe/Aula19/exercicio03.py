'''Criar um script com pyautogui que digite um texto no bloco de notas
copia e cola o mesmo texto em outro bloco de notas'''

import pyautogui
import time

pyautogui.press('winleft')
programa = "Bloco de Notas"
pyautogui.write(programa)
pyautogui.press('enter')
time.sleep(2)

pyautogui.typewrite("Hello, World")
time.sleep(2)


pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')


pyautogui.press('winleft')
programa = "Bloco de Notas"
pyautogui.write(programa)
pyautogui.press('enter')

pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
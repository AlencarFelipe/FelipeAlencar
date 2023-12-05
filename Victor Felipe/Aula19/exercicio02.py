import pyautogui
import time

pyautogui.press('winleft')
programa = "Google Chrome"
pyautogui.write(programa)
pyautogui.press('enter')

time.sleep(2)

pyautogui.typewrite("Rockstar Games")
time.sleep(2)

pyautogui.press("enter")

# Mover o mouse para as coordenadas (x,y) e clique
pyautogui.move(205, 352, duration=1)
pyautogui.click()



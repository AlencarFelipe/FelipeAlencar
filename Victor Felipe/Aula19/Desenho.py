import pyautogui
import time

# Função para desenhar estrela

def desenhar_estrela(x, y,tamanho):
    pyautogui.click(x,y)
# clica no ponto inicial o paint

# calcular pontos da estrela 

    pontas =  5
    angulo = 360
    raio_externo = tamanho
    raio_interno = tamanho/2

    for i in range(pontas*2):
        if 1 % 2 != 0:
            pyautogui.dragRel(raio_interno,0, duration=1)
            # desenha a linha interna 
        else:
            pyautogui.dragRel(raio_externo,0, duration=1)
            # desenha a linha externa 
    pyautogui.moveRel(0,0)

# Aguardar alguns segundos
time.sleep(5)

# Coordenadas do ponto nicial e tamanho da estrela 
x_inicial, y_inicial = 100, 100
tamanho_estrela= 50

desenhar_estrela(10,5,5)


import random
numero_sorteado = random.randint(1,100)
palpite = 0

while (True):
    palpite = int(input("Adivinhe o número :"))
    palpite += 1

    if (palpite > numero_sorteado ):
        print("Tente um numero menor...")
        
    

    elif (palpite < numero_sorteado ):
        print("Tente um numero maior...")
      
    

    else:
        print("Você acertou um numero!!!")
        palpite == numero_sorteado
        break
from time import sleep
import random

ALFABETO = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R','S', 'T', 'U','V', 'W','X','Y','Z']

def sortearLetra():
    while True:
        for i in range(5,0,-1):
            print(i)
            sleep(1)
        letra_sorteada = random.choice(ALFABETO)
        return letra_sorteada
        
letra_sorteada = sortearLetra()
print(f"A letra sorteada é: {letra_sorteada}")

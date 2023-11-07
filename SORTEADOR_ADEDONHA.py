from time import sleep
import random

ALFABETO = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R','S', 'T', 'U','V', 'W','X','Y','Z']
letras_sorteadas = []

def sortearLetra():
    for i in range(5,0,-1):
        print(i)
        sleep(1)
    letra_sorteada = random.choice(ALFABETO)
    if letra_sorteada not in letras_sorteadas:
        letras_sorteadas.append(letra_sorteada)
        ALFABETO.remove(letra_sorteada)
        return letra_sorteada
    else:
        return sortearLetra()

def iniciar_adedonha():
    jogar = True
    while jogar:
        opcao = int(input('1.Para sortear letra.\n2.Para mostrar letras já selecionadas.\n3.Para encerrar jogo'))
        if opcao == 1:
            letra_sorteada = sortearLetra()
            print(f"A letra sorteada é: {letra_sorteada}")
            input('Pressione Enter para continuar...')
        elif opcao == 2:
            print("Letras já selecionadas: ", letras_sorteadas)
        elif opcao == 3:
            jogar = False
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")

if __name__ == "__main__":
    iniciar_adedonha()

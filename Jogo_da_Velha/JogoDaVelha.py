import os
import random
from colorama import Fore, Back, Style

jogarNovamente = 's'
jogadas = 0
quem_joga = 2
maxJogadas = 9
vit = 'n'

velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def Tela():
    os.system('cls')
    print("  0   1   2")
    print(f'0: {velha[0][0]} | {velha[0][1]} | {velha[0][2]}')
    print('   -----------')
    print(f'1: {velha[1][0]} | {velha[1][1]} | {velha[1][2]}')
    print('   -----------')
    print(f'2: {velha[2][0]} | {velha[2][1]} | {velha[2][2]}')
    print(f'Jogadas {Fore.GREEN + str(jogadas) + Fore.RESET}')
    # print(f'Jogadas {str(jogadas)}')


def JogadorJoga():
    global quem_joga
    global jogadas
    if quem_joga == 2 and jogadas < maxJogadas:
        try:
            l = int(input('Linha...: '))
            c = int(input('Coluna.: '))
            while velha[l][c] != ' ':
                l = int(input('Linha...: '))
                c = int(input('Coluna.: '))
            velha[l][c] = "X"
            quem_joga = 1
            jogadas += 1
        except:
            print('Jogada invalida')
            os.system('pause')


def cpuJoga():
    global quem_joga
    global jogadas
    if quem_joga == 1 and jogadas < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != ' ':
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = "O"
        quem_joga = 2
        jogadas += 1


while True:
    Tela()
    JogadorJoga()
    cpuJoga()

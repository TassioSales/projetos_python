import os
import random
from colorama import Fore, Back, Style

jogarNovamente = 's'
jogadas = 0
quem_joga = 2
maxJogadas = 9
vitoria = 'n'

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


def verificarVitoria():
    global velha
    simbolos = ["X", "O"]
    vitoria = 'n'
    for s in simbolos:
        vitoria = "n"
        ilinha = 0
        icoluna = 0
        while ilinha < 3:
            soma = 0
            icoluna = 0
            while icoluna < 3:
                if velha[ilinha][icoluna] == s:
                    soma += 1
                icoluna += 1
            if soma == 3:
                vitoria = s
                break
            ilinha += 1
        if vitoria != "n":
            break
        # verificar vitoris in colunas
        ilinha = 0
        icoluna = 0
        while icoluna < 3:
            soma = 0
            ilinha = 0
            while ilinha < 3:
                if velha[ilinha][icoluna] == s:
                    soma += 1
                ilinha += 1
            if soma == 3:
                vitoria = s
                break
            icoluna += 1
        if vitoria != "n":
            break
        # verificar vitoria diagonal
        soma = 0
        idiag = 0
        while idiag < 3:
            if velha[idiag][idiag] == s:
                soma += 1
            idiag += 1
        if soma == 3:
            vitoria = s
            break
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if velha[idiagl][idiagc] == s:
                soma += 1
            idiagl += 1
            idiagc -= 1
        if soma == 3:
            vitoria = s
            break
    return vitoria


def redefinir():
    global velha
    global jogadas
    global quem_joga
    global maxJogadas
    global vitoria
    global jogarNovamente
    jogarNovamente = 's'
    jogadas = 0
    quem_joga = 2
    maxJogadas = 9
    vitoria = 'n'
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


if __name__ == '__main__':
    while jogarNovamente == "s":
        while True:
            Tela()
            JogadorJoga()
            cpuJoga()
            Tela()
            vit = verificarVitoria()
            if vit != 'n' or jogadas >= maxJogadas:
                break
        print(f"{Fore.RED} Fim de jogo {Fore.YELLOW}")
        if vit == "X" or vit == "o":
            print(f"Resultado: Jogador {vit} venceu")
        else:
            print("Resultado: Empate")
        jogarNovamente = input(f"{Fore.BLUE} Jogar noavamente [s/n] ?: {Fore.RESET}").lower().strip()[0]
        redefinir()

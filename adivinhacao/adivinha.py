import random
import os

erros = 0

sorteados = random.randrange(0,100)

jogador = int(input("Digite seu numero: "))

while sorteados != jogador:
        os.system('cls')
        if sorteados > jogador:
                print("Erro numero e maior")
        elif sorteados < jogador:
                print("Erro numero e menor")
        jogador = int(input("Digite seu numero: "))
        erros += 1

print(f"Numero {jogador} voce acertou em {erros+1}" )

import os

carros = []


class Carro:
    nome = ''
    pot = 0
    velMax = 0
    ligado = False

    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot * 2)
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
        else:
            print("Carro ja esta ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
        else:
            print("Carro ja esta Desligado.")

    def info(self):
        print("Nome......:{}".format(self.nome))
        print("Potencia..:{}".format(self.pot))
        print('Vel.maxima:{}'.format(self.velMax))
        print('Ligado....:{}'.format("Sim" if self.ligado== True else "Nao"))


def menu():
    os.system('cls') or None
    print('1 - Novo Carro')
    print('2 - Informações do carro')
    print('3 - Excluir Carro')
    print('4 - Ligar Carro')
    print('5 - Deligar carro')
    print('6 - Lista carros')
    print('7 - Sair')
    print('Quantidade de carros na lista {}'.format(len(carros)))
    opc = int(input('Digite uma opcão: '))
    return opc


def NovoCarro():
    os.system('cls') or None
    n = input('Digite o nome do carro: ')
    p = (input('Digite a potencia do carro: '))
    car = Carro(n, p)
    carros.append(car)
    print("Novo carro adicionado")
    os.system('pause')
    menu()


def informacoes():
    os.system('cls') or None
    num = input('Informe o numero do carro que deseja ver as informaçoes')
    try:
        carros[int(num)].info()

    except Exception as E:
        print(E)
        print('Carros innexiste na lista')
    os.system('pause')


def ExcluirCarros():
    os.system('cls') or None
    num = input('Informe o numero do carro que deseja ver as informaçoes')
    try:
        del carros[int(num)]
    except Exception as E:
        print(E)
        print('Carros innexiste na lista')
    os.system('pause')


def ligarCarrro():
    os.system('cls') or None
    num = input('Informe o numero do carro que deseja ver as informaçoes')
    try:
        carros[int(num)].ligar()
        print("Carros Ligado ")
    except Exception as E:
        print(E)
        print('Carros innexiste na lista')
    os.system('pause')


def DesligarCarrro():
    os.system('cls') or None
    num = input('Informe o numero do carro que deseja ver as informaçoes')
    try:
        carros[int(num)].desligar()
        print("Carros Desligado ")
    except Exception as E:
        print(E)
        print('Carros innexiste na lista')
    os.system('pause')


def ListarCarros():
    os.system('cls')
    cont = 0
    for c in carros:
        print('{} - {}'.format(cont, c.nome))
        cont += 1
    os.system("pause")


retorno = menu()

try:
    while retorno < 7:
        if retorno == 1:
            NovoCarro()
        elif retorno == 2:
            informacoes()
        elif retorno == 3:
            ExcluirCarros()
        elif retorno == 4:
            ligarCarrro()
        elif retorno == 5:
            DesligarCarrro()
        elif retorno == 6:
            ListarCarros()
        elif retorno == 7:
            break
        else:
            print("Opçao invalida")
except Exception as E:
    print(E.__class__)
    print(E)

os.system('cls') or None
print("Programa finalizado")

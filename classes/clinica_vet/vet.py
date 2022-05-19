import os

pets = []


class Pet:
    def __init__(self, nome, idade, raca, tipo, vacinado=False):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.tipo = tipo
        self.vacinado = vacinado

    def vacinar(self):
        if not self.vacinado:
            self.vacinado = True
        else:
            print("Seu pet ja esta vacinado")

    def info(self):
        print("Nome......:{}".format(self.nome))
        print("Idade.....:{}".format(self.idade))
        print('Raça......:{}'.format(self.raca))
        print('Tipo......:{}'.format(self.tipo))
        print('Vacinado.: {}'.format("Sim" if self.vacinado == True else "Não"))


def menu():
    os.system('cls')
    print('1 - Cadastratar Pet')
    print('2 - Informações do Pet')
    print('3 - Vacinar pet')
    print('4 - Lista de Pets')
    print('5 - Excluir pet da Lista')
    print('6 - Altera dados do Pet')
    print('7 - Sair')
    print('Quantidad de pets na lista {}'.format(len(pets)))
    opc = int(input('Digite a opção desejada: '))
    return opc


def NovoPet():
    os.system('cls')
    nome = input("Digite o nome do pet.........: ")
    idade = int(input("Digite a idade do pet...: "))
    raca = input("Digite e raca do pet........: ")
    Tipo = input("Digite o Tipo do pet.........:")
    while True:
        vacinado = input("O pet esta vacinado [S/N]:").lower().strip()[0]
        if vacinado == "s":
            vacinado = True
            break
        elif vacinado == "n":
            vacinado = False
            break
        else:
            print("Valor digitado incarretamente")
            continue
    pet = Pet(nome, idade, raca, Tipo, vacinado)
    pets.append(pet)
    print("Novo pet adicionado")
    os.system('pause')


def informacoes():
    os.system('cls')
    cont = 0
    for pet in pets:
        print(f'| {cont} | - | {pet.nome} | - | {pet.raca}|')
        cont += 1
    informe = int(input('Informe o o numero de pet que deseja verifcar'))
    try:
        print(Pet.info(pets[informe]))
    except Exception as E:
        print(E)
        print('Carros innexiste na lista')
    os.system('pause')


def vacinar():
    os.system('cls')
    cont = 0
    for pet in pets:
        print(f'| {cont} | - | {pet.nome} | - | {pet.raca} - {pet.vacinado}|')
        cont += 1
    informe = int(input('Informe o pet que deseja vacinar: '))
    try:
        Pet.vacinar(pets[informe])
        print('O pet foi vacinado')
    except Exception as E:
        print(E)
        print(E.__class__())
        print('O pet nao existe na lista')
    os.system('pause')


def listaPet():
    os.system('cls')
    cont = 0
    for pet in pets:
        print(f'| {cont} | - | {pet.nome} | - | {pet.raca} | - | {pet.idade} | - | {pet.tipo} | - | {pet.vacinado} |')
        cont += 1
    os.system('pause')


def ExcluirPet():
    os.system('cls')
    cont = 0
    for pet in pets:
        print(f'| {cont} | - | {pet.nome} | - | {pet.raca} |')
        cont += 1
    informe = input('Informe o numero do pet que deseja excluir: ')
    try:
        del pets[int(informe)]
        print('Pet excluido da lista')
    except Exception as E:
        print(E)
        print('Pet innexiste na lista')
    os.system('pause')


def alteraDados():
    os.system('cls')
    cont = 0
    for pet in pets:
        print(f'| {cont} | - | {pet.nome} | - | {pet.raca} |')
        cont += 1
    informe = int(input('Informe o numero do pet que deseja alterar : '))
    pets[informe].nome = input('informe o Nome..: ')
    pets[informe].idade = input('informe a Idade: ')
    pets[informe].tipo = input('informe a Tipo..: ')
    pets[informe].raca = input('informe o Raça..: ')
    while True:
        pets[informe].vacinado = input("O pet esta vacinado [S/N]:").lower().strip()[0]
        if pets[informe].vacinado == "s":
            pets[informe].vacinado = True
            break
        elif pets[informe].vacinado == "n":
            pets[informe].vacinado = False
            break
        else:
            print("Valor digitado incarretamente")
            continue
    for pet in pets:
        print(f'| {pet.nome} | - | {pet.idade} | - | {pet.tipo} | - | {pet.raca} | - | {pet.vacinado}|')

    os.system('pause')


if __name__ == '__main__':
    retorno = menu()
    try:
        while retorno < 7:
            if retorno == 1:
                NovoPet()
            elif retorno == 2:
                informacoes()
            elif retorno == 3:
                vacinar()
            elif retorno == 4:
                listaPet()
            elif retorno == 5:
                ExcluirPet()
            elif retorno == 6:
                alteraDados()
            elif retorno == 7:
                break
            else:
                print("Opção invalida incorretamente")
            retorno = menu()
    except Exception as E:
        print(E)
        print(E.__class__)

class Carros():
    def __init__(self, nome, modelo, ligado=False):
        self.nome = nome
        self.modelo = modelo
        self.ligado = ligado

    def mostraDados(self):
        print(f'MARCA: {self.nome}')
        print(f"MODELO: {self.modelo}")

    def ligar(self):
        if self.ligado == False:
            self.ligado = True
            print("Ligando carro")
        else:
            print("Carro ja esta ligado")

    def desliga(self):
        if self.ligado == True:
            print("Desligando Carro")
            self.ligado = False
        else:
            print("O carro ja esta desligado")

    def andar(self):
        if self.ligado:
            print("Carro Ja esta Andando")
        else:
            print("Carro esta desligado")
            print('Ligar carro antes')


if __name__ == '__main__':
    c1 = Carros("fiat", 'uno')
    c1.mostraDados()
    c1.ligar()
    c1.andar()
    c1.desliga()
    c1.desliga()

lista = [3, 4, 6, 8, 9,
         0, 2, 3, 4, 5,
         6, 7, 7, 4, 4,
         3, 4, 3, 3, 4,
         2, 5, 2, 4, 3,
         6, 5, 5, 2, 9]


def somar(num):
    resultado = 0
    for n in num:
        resultado += n
    return resultado


if __name__ == '__main__':
    print(somar(lista))

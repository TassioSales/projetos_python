def somar(*numeros):
    soma = 0
    for num in numeros:
        soma += num
    print(f"Soma {soma}")


if __name__ == '__main__':
    somar(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    somar(10, 23)
    somar(8, 6)

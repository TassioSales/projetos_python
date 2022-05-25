carros = ['HRV', 'Polo', 'Jetta', 'Cruze', 'Fusion', 'Palio', 'Gol', 'Fusquinha', 'Focus', 'Onyx', 'Fit']

itCarros = iter(carros)

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration as st:
        print("Fim da lista")
        break

resultado = lambda numero1, numero2: print(numero1 + numero2)
multiplicar = lambda num1, num2: print(num1 * num2)

print((lambda a, b: a - b)(3, 2))

result = lambda x, func: x + func(x)
res = result(2, lambda x: x * x)

print(res)

multiplicar(2, 3)

resultado(3, 5)

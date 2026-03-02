a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))


def quadrado(x):
    return x * x


def somade_quadrados(x, y):
    return quadrado(x) + quadrado(y)


resultado = somade_quadrados(a, b)
print("A soma dos quadrados de", a, "e", b, "é", resultado)
#a = 7
#b = 5
#c = 9

a = input(int("Digite um numero: "))
b = input(int("Digite outro numero: "))

def quadrado(x):
    y = x * x
    return y

def somadeQuadrados(x,y):
    a = quadrado(x)
    b = quadrado(y)
    #c = quadrado(z)
    return a+b

resultado=somadeQuadrados(a,b)
print("a soma dos quadrados de ", a, "e ", b, "é", resultado)


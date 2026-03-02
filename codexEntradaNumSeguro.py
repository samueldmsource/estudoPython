MAX_NUM = 1_000_000
MIN_NUM = -1_000_000
MAX_CARACTER = 20

def entradaNumSeguro(mensagem):
    while True:
        entrada = input(mensagem).strip()

        if not entrada:
            print("Entrada vazia")
            continue

        if len(entrada) > MAX_NUM:
            print("Entrada muito grande, digite ",MAX_CARACTER,"dígitos")
            continue

        sinal = entrada[0] in "+-"
        corpo = entrada[1:] if sinal else entrada

        if not corpo.isdigit():
            print("Digite apenas números")
            continue


        numero = int(entrada)

        if numero < MIN_NUM or numero > MAX_NUM:
            print("número fora do intervalo permitido")
            continue

        return numero

def quadrado (x):
        y = x * x
        return y

def somadeQuadrado(x,y):
    return quadrado(x) + quadrado(y)

a = entradaNumSeguro("digite o primeiro número: ")
b = entradaNumSeguro("digite o segundo número: ")

resultado = somadeQuadrado(a,b)

print("O resultado da soma dos quadrados dos número é: ", resultado)







valor_investido = float(input("Digite o valor que você deseja investir: "))
taxa_juros = float(input("Digite a taxa de juros ao ano (%): "))
tempo_meses = int(input("Digite o tempo em meses: "))

taxa_mensal = (taxa_juros / 100) / 12

montante = valor_investido * (1 + taxa_mensal) ** tempo_meses

print("O montante após o investimento será de: R$", round(montante, 2))
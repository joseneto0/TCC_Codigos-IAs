# Leitura dos valores de entrada
primeira_linha = input().split()
N = int(primeira_linha[0])
R = int(primeira_linha[1])

# Leitura dos valores dos sensores
valores_sensores = list(map(int, input().split()))

# Comparar cada valor dos sensores com o valor de referência R e imprimir o resultado
for valor in valores_sensores:
    if valor <= R:
        print(1)
    else:
        print(0)
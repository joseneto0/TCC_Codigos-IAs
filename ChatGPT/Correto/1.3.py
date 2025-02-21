# Leitura dos dados de entrada
N, R = map(int, input().split())  # N é o número de sensores, R é o valor de referência
sensores = list(map(int, input().split()))  # Lista com os valores dos sensores

# Verificando os sensores
for valor in sensores:
    if valor <= R:
        print(1)
    else:
        print(0)
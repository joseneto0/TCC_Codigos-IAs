# Leitura dos dados
N, R = map(int, input().split())
sensores = list(map(int, input().split()))

# Verificação dos sensores
for sensor in sensores:
    if sensor <= R:
        print(1)
    else:
        print(0)
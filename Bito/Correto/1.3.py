# Lendo a entrada
N, R = map(int, input().split())
sensores = list(map(int, input().split()))

# Verificando cada sensor e imprimindo o resultado
for valor in sensores:
    if valor <= R:
        print(1)
    else:
        print(0)
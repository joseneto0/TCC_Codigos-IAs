# Lendo a entrada
N, E = map(int, input().split())
total_colhido = 0

# Lendo o número de melões colhidos por cada produtor
for _ in range(N):
    melões_colhidos = int(input())
    total_colhido += melões_colhidos

# Comparando o total colhido com o total esperado
if total_colhido >= E:
    print("NADA PREOCUPANTE")
elif total_colhido >= E - 5:
    print("POUCO PREOCUPANTE")
else:
    print("MUITO PREOCUPANTE")
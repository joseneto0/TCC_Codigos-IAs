# Leitura da entrada
N, E = map(int, input().split())  # N é o número de produtores, E é o valor esperado
total_colhido = 0  # Variável para armazenar o total de melões colhidos

# Somando a quantidade de melões colhidos por cada produtor
for _ in range(N):
    total_colhido += int(input())

# Comparando o total colhido com o total esperado
if total_colhido >= E:
    print("NADA PREOCUPANTE")
elif total_colhido >= E - 5:
    print("POUCO PREOCUPANTE")
else:
    print("MUITO PREOCUPANTE")
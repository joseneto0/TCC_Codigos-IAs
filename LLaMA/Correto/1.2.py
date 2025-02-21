# Leitura dos dados
N, E = map(int, input().split())

# Inicialização da variável para armazenar o total de melões colhidos
total_colhido = 0

# Leitura e soma dos melões colhidos por cada produtor
for _ in range(N):
    total_colhido += int(input())

# Verificação da situação
if total_colhido >= E:
    print("NADA PREOCUPANTE")
elif total_colhido >= E - 5:
    print("POUCO PREOCUPANTE")
else:
    print("MUITO PREOCUPANTE")
# Leitura do número de sensores
N = int(input())

# Leitura dos valores de ativação dos sensores
valores = [int(input()) for _ in range(N)]

# Inicialização da variável para armazenar a quantidade de armadilhas
armadilhas = 0

# Verificação dos valores de ativação
for i in range(N):
    if valores[i] == 1 and (i == 0 or valores[i-1] == 0):
        armadilhas += 1

# Impressão da quantidade de armadilhas
print(armadilhas)

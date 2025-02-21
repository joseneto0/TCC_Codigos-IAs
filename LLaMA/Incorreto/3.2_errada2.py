# Leitura do número de casas
N = int(input())

# Leitura da quantidade de moedas em cada casa
moedas = list(map(int, input().split()))

# Inicialização da variável para armazenar o número de turnos
turnos = 0

# Loop para processar as moedas
for i in range(N // 2):
    turnos += abs(i - (N // 2)) + max(moedas[i], moedas[N - i - 1])

# Impressão do número de turnos
print(turnos)

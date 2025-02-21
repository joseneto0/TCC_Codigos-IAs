# Lendo o número de casas
N = int(input())

# Lendo a quantidade de moedas em cada casa
moedas = list(map(int, input().split()))

# A posição do buraco é a casa central
buraco = N // 2

# Inicializando o contador de turnos
turnos = 0

# Calculando os turnos necessários para as casas à esquerda do buraco
for i in range(buraco):
    turnos += moedas[i] * (buraco - i)

# Calculando os turnos necessários para as casas à direita do buraco
for i in range(buraco + 1, N):
    turnos += moedas[i] * (i - buraco)

# Imprimindo o total de turnos
print(turnos)
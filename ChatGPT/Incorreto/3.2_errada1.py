def calcular_turnos(N, moedas):
    centro = N // 2  # O buraco está na posição central (índice N//2)
    turnos = 0
    
    # Percorrer as casas à esquerda e à direita do buraco
    for i in range(N):
        if i != centro:  # Ignorar o buraco
            turnos += abs(i - centro) * moedas[i]  # Distância * quantidade de moedas
    
    return turnos

# Leitura da entrada
N = int(input())  # Lê o número de casas (ímpar)
moedas = list(map(int, input().split()))  # Lê as moedas em cada casa

# Calcula e imprime o resultado
print(calcular_turnos(N, moedas))
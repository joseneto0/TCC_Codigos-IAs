def calcular_turnos(N, moedas):
    centro = N // 2  # O buraco está na posição central (índice N//2)
    turnos = 0
    
    # Calcular a soma das distâncias * quantidade de moedas
    for i in range(N):
        if i != centro:  # Ignorar o buraco
            dist = abs(i - centro)  # Distância da casa ao buraco
            turnos += dist * moedas[i]  # Multiplicar pela quantidade de moedas
    
    return turnos

# Leitura da entrada
N = int(input())  # Lê o número de casas (ímpar)
moedas = list(map(int, input().split()))  # Lê as moedas em cada casa

# Calcula e imprime o resultado
print(calcular_turnos(N, moedas))
def calcular_turnos():
    # Lê o número de casas
    N = int(input())
    
    # Lê as moedas em cada casa
    moedas = list(map(int, input().split()))
    
    # Calcula a posição do buraco central
    centro = (N - 1) // 2
    
    # Calcula o número total de turnos
    turnos = 0
    for i in range(N):
        if i != centro:
            turnos += moedas[i]
    
    # Imprime o número de turnos
    print(turnos)

# Chama a função para calcular os turnos
calcular_turnos()
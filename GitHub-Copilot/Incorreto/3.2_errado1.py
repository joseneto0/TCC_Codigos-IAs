def calcular_min_turnos(n, moedas):
    buraco_central = n // 2
    turnos = 0

    for i in range(n):
        if i != buraco_central:
            turnos += moedas[i] * abs(i - buraco_central)
    
    return turnos

# Leitura da entrada
n = int(input().strip())
moedas = list(map(int, input().strip().split()))

# Calcular e imprimir a quantidade mínima de turnos
resultado = calcular_min_turnos(n, moedas)
print(resultado)
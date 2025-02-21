def calcular_min_turnos(n, moedas):
    buraco_central = n // 2
    turnos = 0

    # Mover moedas da esquerda do buraco central
    for i in range(buraco_central - 1, -1, -1):
        if moedas[i] > 0:
            distancia = buraco_central - i
            turnos += moedas[i] * distancia

    # Mover moedas da direita do buraco central
    for i in range(buraco_central + 1, n):
        if moedas[i] > 0:
            distancia = i - buraco_central
            turnos += moedas[i] * distancia

    return turnos

# Leitura da entrada
n = int(input().strip())
moedas = list(map(int, input().strip().split()))

# Calcular e imprimir a quantidade mínima de turnos
resultado = calcular_min_turnos(n, moedas)
print(resultado)
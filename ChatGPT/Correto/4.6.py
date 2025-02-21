# Função que simula os turnos até que todos os slimes se tornem sementes
def calcular_turnos(slimes):
    turnos = 0
    # Continuamos enquanto houver slimes com tamanho maior que 1
    while any(slime > 1 for slime in slimes):
        turnos += 1
        # Para cada slime, aplicamos a regra
        for i in range(len(slimes)):
            if slimes[i] > 1:
                if slimes[i] % 2 == 0:  # Se for par
                    slimes[i] //= 2
                else:  # Se for ímpar
                    slimes[i] += 1
    return turnos

# Leitura da entrada
slimes = list(map(int, input().split()))

# Chama a função que calcula os turnos necessários
turnos = calcular_turnos(slimes)

# Imprime a quantidade de turnos
print(turnos)
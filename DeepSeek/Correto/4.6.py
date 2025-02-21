def calcular_turnos(slimes):
    turnos = 0
    while any(slime > 1 for slime in slimes):
        novos_slimes = []
        for slime in slimes:
            if slime > 1:
                if slime % 2 == 0:
                    novos_slimes.append(slime // 2)
                    novos_slimes.append(slime // 2)
                else:
                    novos_slimes.append(slime + 1)
            else:
                novos_slimes.append(slime)
        slimes = novos_slimes
        turnos += 1
    return turnos

# Leitura da entrada
slimes = list(map(int, input().split()))

# Cálculo dos turnos
turnos = calcular_turnos(slimes)

# Saída
print(turnos)
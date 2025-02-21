# Lendo os tamanhos iniciais dos slimes
slimes = list(map(int, input().strip().split()))

# Inicializando o contador de turnos
turnos = 0

# Enquanto houver slimes com tamanho maior que 1
while any(size > 1 for size in slimes):
    turnos += 1
    for i in range(len(slimes)):
        if slimes[i] > 1:
            if slimes[i] % 2 == 0:
                slimes[i] //= 2  # Dividir o slime
            else:
                slimes[i] += 1  # Crescer o slime

# Imprimindo o número de turnos
print(turnos)
# Leitura dos tamanhos iniciais dos slimes
tamanhos = list(map(int, input().split()))

# Inicialização da variável para armazenar o número de turnos
turnos = 0

# Loop para processar os slimes
while True:
    # Verificação se todos os slimes se transformaram em sementes
    if all(tamanho <= 1 for tamanho in tamanhos):
        break

    # Processamento dos slimes
    tamanhos = [tamanho + 1 if tamanho % 2 != 0 else tamanho // 2 for tamanho in tamanhos]

    # Incremento do número de turnos
    turnos += 1

# Impressão do número de turnos
print(turnos)

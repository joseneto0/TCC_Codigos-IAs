# Leitura dos tamanhos iniciais dos slimes
tamanhos = list(map(int, input().split()))

# Função recursiva para processar os slimes
def processar_slimes(tamanhos, turnos=0):
    if all(tamanho <= 1 for tamanho in tamanhos):
        return turnos
    else:
        tamanhos = [tamanho + 1 if tamanho % 2 != 0 else tamanho // 2 for tamanho in tamanhos]
        return processar_slimes(tamanhos, turnos + 1)

# Impressão do número de turnos
print(processar_slimes(tamanhos))

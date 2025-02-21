# Leitura do número de sensores
N = int(input())

# Leitura dos valores dos sensores
sensores = [int(input()) for _ in range(N)]

# Inicialização do contador de armadilhas
armadilhas = 0

# Variável para marcar se estamos em um segmento de sensores ativados
em_segmento = False

# Percorrer a lista de sensores
for sensor in sensores:
    if sensor == 1:
        if not em_segmento:
            # Início de um novo segmento
            armadilhas += 1
            em_segmento = True
    else:
        # Fim do segmento atual
        em_segmento = False

# Imprimir a quantidade mínima de armadilhas
print(armadilhas)
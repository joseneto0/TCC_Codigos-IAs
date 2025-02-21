# Lendo o número de sensores
N = int(input())
sensores = [int(input()) for _ in range(N)]

# Inicializando a contagem de armadilhas
armadilhas = 0
em_atividade = False

# Percorrendo a lista de sensores
for valor in sensores:
    if valor == 1:
        if not em_atividade:
            # Iniciando um novo grupo de sensores ativados
            armadilhas += 1
            em_atividade = True
    else:
        # Sensor não ativado, encerrando o grupo
        em_atividade = False

# Imprimindo a quantidade mínima de armadilhas
print(armadilhas)
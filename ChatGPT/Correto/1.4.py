# Programa para determinar a quantidade mínima de armadilhas necessárias

def calcular_armadilhas(n, sensores):
    # Inicializa o contador de armadilhas
    armadilhas = 0
    i = 0

    # Percorre a lista de sensores
    while i < n:
        if sensores[i] == 1:  # Encontra um sensor ativado
            armadilhas += 1  # Adiciona uma armadilha para este segmento contíguo
            while i < n and sensores[i] == 1:
                i += 1  # Pula todos os sensores contíguos ativados
        else:
            i += 1  # Pula os sensores não ativados

    return armadilhas

# Leitura da entrada
n = int(input())
sensores = [int(input()) for _ in range(n)]

# Calcula e imprime o resultado
resultado = calcular_armadilhas(n, sensores)
print(resultado)
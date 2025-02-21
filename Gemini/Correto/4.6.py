def contar_turnos(tamanhos):
    turnos = 0
    while any(tamanho > 1 for tamanho in tamanhos):
        novos_tamanhos = []
        for tamanho in tamanhos:
            if tamanho == 1:
                continue
            elif tamanho % 2 == 0:
                novos_tamanhos.extend([tamanho // 2] * 2)
            else:
                novos_tamanhos.append(tamanho + 1)
        tamanhos = novos_tamanhos
        turnos += 1
    return turnos

# Leitura da entrada
tamanhos = list(map(int, input().split()))

# Chama a função para contar os turnos
resultado = contar_turnos(tamanhos)

# Imprime o resultado
print(resultado)
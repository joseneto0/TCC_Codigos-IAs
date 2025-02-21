def calcular_beleza(verso1, verso2):
    # Extrai as últimas palavras dos versos
    palavra1 = verso1.split()[-1]
    palavra2 = verso2.split()[-1]
    
    # Inicializa a contagem de beleza
    beleza = 0
    # Verifica as letras iguais do final das palavras
    for i in range(1, min(len(palavra1), len(palavra2)) + 1):
        if palavra1[-i] == palavra2[-i]:
            beleza += 1
        else:
            break
    return beleza

# Leitura da entrada
versos = [input().strip() for _ in range(4)]

# Calcular a beleza das rimas
beleza_poema = calcular_beleza(versos[0], versos[2]) + calcular_beleza(versos[1], versos[3])

# Resultado
print(beleza_poema)
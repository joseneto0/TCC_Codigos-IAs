def obter_ultima_palavra(verso):
    # Divide o verso em palavras e retorna a última palavra
    palavras = verso.split()
    return palavras[-1]

def calcular_beleza(palavra1, palavra2):
    # Calcula a beleza da rima entre duas palavras
    tamanho = min(len(palavra1), len(palavra2))
    beleza = 0
    for i in range(1, tamanho + 1):
        if palavra1[-i] == palavra2[-i]:
            beleza += 1
        else:
            break
    return beleza

def calcular_beleza_poema(versos):
    # Extrai a última palavra de cada verso
    ultima_palavra1 = obter_ultima_palavra(versos[0])
    ultima_palavra2 = obter_ultima_palavra(versos[1])
    ultima_palavra3 = obter_ultima_palavra(versos[2])
    ultima_palavra4 = obter_ultima_palavra(versos[3])
    
    # Calcula a beleza das rimas
    beleza_rima1 = calcular_beleza(ultima_palavra1, ultima_palavra3)
    beleza_rima2 = calcular_beleza(ultima_palavra2, ultima_palavra4)
    
    # Soma as belezas das rimas
    beleza_total = beleza_rima1 + beleza_rima2
    return beleza_total

# Leitura dos versos
versos = [input().strip() for _ in range(4)]

# Cálculo da beleza do poema
beleza_poema = calcular_beleza_poema(versos)

# Impressão do resultado
print(beleza_poema)
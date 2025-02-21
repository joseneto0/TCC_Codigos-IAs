# Função para extrair a última palavra de um verso
def ultima_palavra(verso):
    return verso.strip().split()[-1]

# Função para calcular a beleza da rima
def beleza_rima(palavra1, palavra2):
    # Contar letras iguais no final das duas palavras
    contagem = 0
    min_length = min(len(palavra1), len(palavra2))
    
    # Verificando as letras do final para o início
    for i in range(1, min_length + 1):
        if palavra1[-i] == palavra2[-i]:
            contagem += 1
        else:
            break  # Se as letras não forem iguais, parar a contagem
    
    return contagem

# Lendo os 4 versos
verso1 = input()
verso2 = input()
verso3 = input()
verso4 = input()

# Extraindo as últimas palavras
ultima_palavra1 = ultima_palavra(verso1)
ultima_palavra2 = ultima_palavra(verso2)
ultima_palavra3 = ultima_palavra(verso3)
ultima_palavra4 = ultima_palavra(verso4)

# Calculando a beleza total do poema
beleza = (beleza_rima(ultima_palavra1, ultima_palavra3) +
          beleza_rima(ultima_palavra2, ultima_palavra4))

# Imprimindo a beleza do poema
print(beleza)
def calcular_tamanho_sequencia(N):
    # Inicializa o contador com 1 porque começamos com o próprio N
    contador = 1
    
    # Enquanto N for maior que 1, continue dividindo por 2
    while N > 1:
        N //= 2
        contador += 1
    
    return contador

# Leitura da entrada
N = int(input().strip())

# Calcula e imprime o tamanho da sequência
resultado = calcular_tamanho_sequencia(N)
print(resultado)
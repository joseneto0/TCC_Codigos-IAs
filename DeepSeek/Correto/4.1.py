def tamanho_sequencia(N):
    contador = 1  # Inclui o próprio N
    while N > 1:
        N = N // 2  # Divide por 2 e descarta a parte fracionária
        contador += 1
    return contador

# Leitura da entrada
N = int(input())

# Cálculo do tamanho da sequência
resultado = tamanho_sequencia(N)

# Saída
print(resultado)
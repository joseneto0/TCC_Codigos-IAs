def gerar_sequencia(N):
    while N != 1:
        print(N)
        if N % 2 == 0:
            N = N // 2
        else:
            N = 3 * N + 1
    print(N)  # Imprime o último valor (1)

# Leitura da entrada
N = int(input())

# Geração da sequência
gerar_sequencia(N)
# Leitura do valor de N
N = int(input())

# Loop para gerar a sequência
while N > 1:
    print(N)

    # Verificação se N é par ou ímpar
    if N % 2 == 0:
        N = N // 2
    else:
        N = 3 * N + 1

# Impressão do último valor da sequência
print(N)
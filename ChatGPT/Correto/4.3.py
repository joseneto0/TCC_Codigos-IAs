# Leitura do número inicial de ar
N = int(input())

# Loop para gerar a sequência até N se tornar 1
while N != 1:
    print(N)
    if N % 2 == 0:  # Se N é par
        N //= 2
    else:  # Se N é ímpar
        N = 3 * N + 1

# Quando N for igual a 1, imprima o último valor
print(1)
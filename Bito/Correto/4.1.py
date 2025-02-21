# Lendo o número N da entrada
N = int(input())

# Inicializando o contador
contador = 0

# Enquanto N for maior que 1
while N > 1:
    contador += 1
    N //= 2  # Divisão inteira por 2

# Adicionando 1 para incluir o último número (1)
contador += 1

# Imprimindo o tamanho da sequência
print(contador)
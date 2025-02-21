# Leitura do número N
N = int(input())

# Inicialização da variável para armazenar o tamanho da sequência
tamanho = 1

# Loop para gerar a sequência
while N > 1:
    N = N // 2
    tamanho += 1

# Impressão do tamanho da sequência
print(tamanho)

# Lendo o número de mensagens
N = int(input())

# Inicializando o contador de mensagens que falam de fadas
contador_fadas = 0

# Processando cada mensagem
for _ in range(N):
    mensagem = input().strip()
    # Dividindo a mensagem em palavras e verificando se "fada" está presente
    palavras = mensagem.split()
    if "fada" in [palavra.lower() for palavra in palavras]:
        contador_fadas += 1

# Imprimindo o resultado
print(contador_fadas)
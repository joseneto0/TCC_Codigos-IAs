# Lendo o número de mensagens
N = int(input())

# Inicializando o contador de mensagens que falam de fadas
contador_fadas = 0

# Processando cada mensagem
for _ in range(N):
    mensagem = input().strip()
    # Dividindo a mensagem em palavras
    palavras = mensagem.split()
    
    # Verificando se "fada" está presente como uma palavra isolada
    for palavra in palavras:
        # Removendo pontuação e convertendo para minúsculas
        palavra_limpa = ''.join(char for char in palavra if char.isalnum()).lower()
        if palavra_limpa == "fada":
            contador_fadas += 1
            break  # Se encontrarmos "fada", não precisamos verificar mais palavras

# Imprimindo o resultado
print(contador_fadas)
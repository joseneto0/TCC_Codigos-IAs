# Leitura do número de mensagens
N = int(input())

# Inicialização da variável para armazenar o número de mensagens que falam de fadas
num_mensagens_fadas = 0

# Loop para processar as mensagens
for _ in range(N):
    # Leitura da mensagem
    mensagem = input()

    # Verificação se a mensagem fala de fadas
    if 'fada' in mensagem.lower():
        num_mensagens_fadas += 1

# Impressão do número de mensagens que falam de fadas
print(num_mensagens_fadas)

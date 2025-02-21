def conta_mensagens_com_fada(mensagens):
    contador = 0
    
    for mensagem in mensagens:
        # Dividir a mensagem em palavras
        palavras = mensagem.split()
        for palavra in palavras:
            # Remover pontuação ao redor da palavra e verificar se é "fada"
            palavra_limpa = ''.join([c for c in palavra if c.isalpha()])
            if palavra_limpa.lower() == 'fada':
                contador += 1
                break  # Encontramos "fada" nesta mensagem, não precisamos verificar mais palavras
    
    return contador

# Leitura do número de mensagens
N = int(input().strip())

# Leitura das mensagens
mensagens = [input().strip() for _ in range(N)]

# Contagem de mensagens que falam de "fada"
resultado = conta_mensagens_com_fada(mensagens)

# Impressão do resultado
print(resultado)
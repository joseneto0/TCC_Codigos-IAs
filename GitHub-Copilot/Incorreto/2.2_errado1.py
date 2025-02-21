import re

def conta_mensagens_com_fada(mensagens):
    # Expressão regular para encontrar a palavra "fada" isolada (case insensitive)
    padrao = re.compile(r'\bfada\b', re.IGNORECASE)
    contador = 0
    
    for mensagem in mensagens:
        # Se a palavra "fada" isolada for encontrada na mensagem, incrementa o contador
        if padrao.search(mensagem):
            contador += 1
    
    return contador

# Leitura do número de mensagens
N = int(input().strip())

# Leitura das mensagens
mensagens = [input().strip() for _ in range(N)]

# Contagem de mensagens que falam de "fada"
resultado = conta_mensagens_com_fada(mensagens)

# Impressão do resultado
print(resultado)
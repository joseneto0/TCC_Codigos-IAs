import re

def contar_fadas(n, mensagens):
    contador = 0
    padrao = r'\bfada\b'  # Palavra "fada" isolada
    for mensagem in mensagens:
        if re.search(padrao, mensagem, re.IGNORECASE):  # Ignora maiúsculas/minúsculas
            contador += 1
    return contador

# Leitura de entrada
n = int(input())  # Número de mensagens
mensagens = [input().strip() for _ in range(n)]  # Lista de mensagens

# Resultado
print(contar_fadas(n, mensagens))
# Inicialização do dicionário para armazenar os tipos de sementes e suas quantidades
sementes = {}

# Loop para processar as linhas da entrada
while True:
    # Leitura da linha
    linha = input()

    # Verificação se a linha é a palavra FIM
    if linha == 'FIM':
        break

    # Verificação se o tipo de semente já está no dicionário
    if linha in sementes:
        # Incremento da quantidade da semente
        sementes[linha] += 1
    else:
        # Adição da semente ao dicionário com quantidade 1
        sementes[linha] = 1

    # Impressão do tipo de semente e sua quantidade
    print(f"{linha} {sementes[linha]}")

# Leitura do texto criptografado
texto_criptografado = input()

# Decodificação do texto
texto_decodificado = ''
i = 0
while i < len(texto_criptografado):
    if texto_criptografado[i] == 'P':
        if i + 1 < len(texto_criptografado) and texto_criptografado[i + 1] == 'P':
            i += 2
            continue
    texto_decodificado += texto_criptografado[i]
    i += 1

# Impressão do texto decodificado
print(texto_decodificado)

def decodificar_lingua_do_p(texto_criptografado):
    texto_decodificado = ""
    i = 0
    while i < len(texto_criptografado):
        if texto_criptografado[i] == 'P' and i + 1 < len(texto_criptografado):
            texto_decodificado += texto_criptografado[i + 1]
            i += 2  # Pular o próximo caractere, pois já foi adicionado
        else:
            texto_decodificado += texto_criptografado[i]
            i += 1
    return texto_decodificado

# Leitura do texto criptografado
texto_criptografado = input().strip()

# Decodificação do texto
texto_decodificado = decodificar_lingua_do_p(texto_criptografado)

# Impressão do texto decodificado
print(texto_decodificado)
def decodificar_lingua_do_p(texto_criptografado):
    # Remove todas as ocorrências de 'P' do texto
    texto_decodificado = texto_criptografado.replace('P', '')
    return texto_decodificado

# Leitura do texto criptografado
texto_criptografado = input().strip()

# Decodificação do texto
texto_decodificado = decodificar_lingua_do_p(texto_criptografado)

# Impressão do texto decodificado
print(texto_decodificado)
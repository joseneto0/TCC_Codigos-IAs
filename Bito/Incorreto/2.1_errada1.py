# Lendo a entrada
texto_criptografado = input()

# Removendo todas as letras 'P' e 'p'
texto_decodificado = texto_criptografado.replace('P', '').replace('p', '')

# Imprimindo o texto decodificado
print(texto_decodificado)
# Leitura do texto criptografado
texto_criptografado = input()

# Decodificação do texto
texto_decodificado = ''
for caractere in texto_criptografado:
    if caractere == 'P':
        continue
    texto_decodificado += caractere

# Impressão do texto decodificado
print(texto_decodificado)

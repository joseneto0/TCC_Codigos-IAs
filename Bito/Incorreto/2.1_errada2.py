# Lendo a entrada
texto_criptografado = input()

# Inicializando uma nova string para o texto decodificado
texto_decodificado = ""

# Usando um índice para percorrer o texto
i = 0
while i < len(texto_criptografado):
    if texto_criptografado[i] == 'P' or texto_criptografado[i] == 'p':
        # Pular todos os 'P' ou 'p' consecutivos
        while i < len(texto_criptografado) and (texto_criptografado[i] == 'P' or texto_criptografado[i] == 'p'):
            i += 1
    else:
        # Adiciona o caractere à nova string se não for 'P' ou 'p'
        texto_decodificado += texto_criptografado[i]
        i += 1

# Imprimindo o texto decodificado
print(texto_decodificado)
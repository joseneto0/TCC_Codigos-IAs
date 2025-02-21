def decodificar_lingua_do_p(texto):
    palavras = texto.split()  # Divide o texto em palavras
    resultado = []  # Lista para armazenar palavras decodificadas

    for palavra in palavras:
        decodificada = ""
        i = 0
        while i < len(palavra):
            if palavra[i] == 'P' and i + 1 < len(palavra):  # Se encontrar 'P' antes de uma letra
                decodificada += palavra[i + 1]  # Adiciona a letra após 'P'
                i += 2  # Pula o 'P' e a letra
            else:
                decodificada += palavra[i]  # Mantém pontuações e outros caracteres
                i += 1
        
        resultado.append(decodificada)  # Adiciona a palavra decodificada

    return " ".join(resultado)  # Junta as palavras de volta em uma única string


# Entrada
texto_criptografado = input()

# Saída
print(decodificar_lingua_do_p(texto_criptografado))
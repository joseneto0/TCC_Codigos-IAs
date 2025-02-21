def decodificar_mensagem(mensagem_criptografada):
    mensagem_decodificada = ""
    i = 0
    while i < len(mensagem_criptografada):
        # Mantemos o caractere atual e pulamos o próximo (que é um 'P' inserido)
        mensagem_decodificada += mensagem_criptografada[i]
        i += 2  # Pulamos o 'P' inserido
    return mensagem_decodificada

# Exemplo de uso
mensagem_criptografada = input().strip()
mensagem_decodificada = decodificar_mensagem(mensagem_criptografada)
print(mensagem_decodificada)
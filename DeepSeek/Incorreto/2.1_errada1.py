def decodificar_mensagem(mensagem_criptografada):
    # Remove todas as ocorrências da letra 'P'
    mensagem_decodificada = mensagem_criptografada.replace('P', '')
    return mensagem_decodificada

# Exemplo de uso
mensagem_criptografada = input().strip()
mensagem_decodificada = decodificar_mensagem(mensagem_criptografada)
print(mensagem_decodificada)
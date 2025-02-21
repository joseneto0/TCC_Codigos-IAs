def contar_mensagens_sobre_fadas(mensagens):
  """Conta o número de mensagens que mencionam a palavra "fada".

  Args:
    mensagens: Lista de mensagens.

  Returns:
    Número de mensagens que mencionam "fada".
  """

  contador = 0
  for mensagem in mensagens:
    if "fada" in mensagem.lower():
      contador += 1
  return contador

# Lendo a entrada
num_mensagens = int(input())
mensagens = [input() for _ in range(num_mensagens)]

# Chamando a função e imprimindo o resultado
resultado = contar_mensagens_sobre_fadas(mensagens)
print(resultado)
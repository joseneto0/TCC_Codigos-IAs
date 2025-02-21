def beleza_do_poema():
  """Calcula a beleza de um poema de 4 versos.

  Returns:
    Um inteiro representando a beleza do poema.
  """

  versos = [input().strip().split()[-1] for _ in range(4)]
  beleza = 0

  for i in range(0, 4, 2):
      palavra1 = versos[i]
      palavra2 = versos[i+1]
      comprimento_comum = 0
      for j in range(min(len(palavra1), len(palavra2))):
          if palavra1[j] == palavra2[j]:
              comprimento_comum += 1
          else:
              break
      beleza += comprimento_comum

  return beleza

# Chamando a função e imprimindo o resultado
resultado = beleza_do_poema()
print(resultado)
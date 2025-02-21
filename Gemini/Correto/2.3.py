def nomes_unicos(nomes):
  """Remove nomes duplicados de uma lista de nomes.

  Args:
    nomes: Lista de nomes.

  Returns:
    Lista de nomes únicos, preservando a ordem original.
  """

  nomes_unicos = []
  for nome in nomes:
    if nome not in nomes_unicos:
      nomes_unicos.append(nome)
  return nomes_unicos

# Lendo a entrada
num_habitantes = int(input())
nomes = [input() for _ in range(num_habitantes)]

# Chamando a função e imprimindo o resultado
resultado = nomes_unicos(nomes)
for nome in resultado:
  print(nome)
def defender_meloes(populacao):
  melões_roubados = 0
  goblins_resgatados = 0

  while True:
    linha = input().split()
    if linha == ['0', '0', '0']:
      break
    forca, melões, goblins = map(int, linha)
    if forca > populacao:
      melões_roubados += melões
      goblins_resgatados += goblins
    print(f"Meloes roubados: {melões_roubados}")
    print(f"Goblins resgatados: {goblins_resgatados}")
    print("---")

# Lendo a entrada
populacao = int(input())

# Chamando a função
defender_meloes(populacao)
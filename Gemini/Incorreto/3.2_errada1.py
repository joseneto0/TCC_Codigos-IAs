def min_turnos(moedas):
    """Calcula o número mínimo de turnos para mover todas as moedas para o buraco.

    Args:
        moedas: Uma lista representando o número de moedas em cada casa.

    Returns:
        O número mínimo de turnos.
    """

    n = len(moedas)
    buraco = n // 2
    turnos = 0

    while any(moedas):  # Enquanto houver moedas fora do buraco
        # Encontrar a pilha mais distante do buraco em cada lado
        esquerda = max(range(buraco), key=lambda i: moedas[i])
        direita = min(range(buraco+1, n), key=lambda i: moedas[i], default=buraco)
        mais_distante = esquerda if moedas[esquerda] > moedas[direita] else direita

        # Mover todas as moedas da pilha mais distante para o buraco
        turnos += moedas[mais_distante]
        moedas[mais_distante] = 0

    return turnos

# Leitura da entrada
n = int(input())
moedas = list(map(int, input().split()))

# Cálculo e impressão do resultado
resultado = min_turnos(moedas)
print(resultado)
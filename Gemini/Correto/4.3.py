def sequencia_glooid(n):
    """Gera a sequência de valores de ar nos pulmões de Glooid.

    Args:
        n: A quantidade inicial de ar.

    Returns:
        Uma lista com a sequência gerada.
    """

    sequencia = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequencia.append(n)
    return sequencia

# Leitura da entrada
n = int(input())

# Geração e impressão da sequência
sequencia = sequencia_glooid(n)
for numero in sequencia:
    print(numero)
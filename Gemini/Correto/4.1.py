def contar_passos(n):
    """Conta quantos passos são necessários para chegar a 1 dividindo por 2 repetidamente.

    Args:
        n: O número inicial.

    Returns:
        O número de passos.
    """

    passos = 0
    while n > 1:
        n //= 2
        passos += 1
    return passos + 1  # Adicionamos 1 para contar o número inicial

# Leitura da entrada
n = int(input())

# Cálculo e impressão do resultado
resultado = contar_passos(n)
print(resultado)
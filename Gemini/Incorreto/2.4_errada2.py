def beleza_do_poema():
    """Calcula a beleza de um poema seguindo as regras especificadas.

    Returns:
        int: A beleza total do poema.
    """

    # Cria uma lista para armazenar os versos
    versos = []
    for _ in range(4):
        verso = input()
        versos.append(verso)

    # Separa as últimas palavras de cada verso
    palavras = [verso.split()[-1] for verso in versos]

    # Compara as rimas e calcula a beleza
    beleza_rima1 = sum(1 for letra1, letra2 in zip(palavras[0][::-1], palavras[2][::-1]) if letra1 == letra2)
    beleza_rima2 = sum(1 for letra1, letra2 in zip(palavras[1][::-1], palavras[3][::-1]) if letra1 == letra2)

    return beleza_rima1 + beleza_rima2

# Chama a função para calcular a beleza do poema
resultado = beleza_do_poema()
print(resultado)
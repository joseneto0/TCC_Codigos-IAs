from collections import defaultdict

def contar_sementes(sementes):
    """Conta a quantidade de cada tipo de semente.

    Args:
        sementes: Uma lista de strings representando os tipos de sementes.

    Returns:
        Um dicionário onde as chaves são os tipos de sementes e os valores são as quantidades.
    """

    contagem = defaultdict(int)
    for semente in sementes:
        contagem[semente] += 1
    return contagem

# Leitura da entrada
sementes = []
while True:
    semente = input()
    if semente == "FIM":
        break
    sementes.append(semente)

# Contagem das sementes
resultado = contar_sementes(sementes)

# Impressão do resultado (corrigida)
for semente, quantidade in resultado.items():
    print(f"{semente} {quantidade}")
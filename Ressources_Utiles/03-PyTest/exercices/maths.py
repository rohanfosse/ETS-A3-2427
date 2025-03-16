def factorielle(n):
    """Calcule la factorielle d'un nombre entier positif."""
    if n < 0:
        raise ValueError("Nombre négatif non autorisé")
    if n == 0:
        return 1
    return n * factorielle(n - 1)

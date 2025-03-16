# **Exercice : Tester une Fonction Mathématique avec Pytest**

## **Objectif**

L'objectif de cet exercice est d’écrire des **tests unitaires** pour vérifier le bon fonctionnement d’une fonction mathématique.  
Vous devrez :

1. Tester plusieurs cas avec `assert`.
2. Vérifier que les erreurs sont bien levées avec `pytest.raises()`.
3. Utiliser `@pytest.mark.parametrize` pour éviter les répétitions.

---

## **1. Fonction à Tester**

Vous devez tester la fonction suivante, qui calcule la factorielle d’un nombre :

📄 **Fichier : `maths.py`**

```python
def factorielle(n):
    """Calcule la factorielle d'un nombre entier positif."""
    if n < 0:
        raise ValueError("Nombre négatif non autorisé")
    if n == 0:
        return 1
    return n * factorielle(n - 1)
```

---

## **2. Consignes**

- Vérifier que `factorielle(5)` retourne `120`.
- Tester `factorielle(0)` et `factorielle(1)`.
- Vérifier que `factorielle(-1)` **lève une erreur** avec `pytest.raises()`.
- Utiliser `@pytest.mark.parametrize` pour tester plusieurs valeurs en une seule fonction.

---


## **3. Fichier de Test à Compléter**

📄 **Fichier : `test_maths.py`**

```python
import pytest
from maths import factorielle

def test_factorielle():
    """Test des valeurs classiques de la factorielle."""
    assert factorielle(5) == 120
    assert factorielle(0) == 1
    assert factorielle(1) == 1

def test_erreur_factorielle():
    """Test si une erreur est levée pour une valeur négative."""
    with pytest.raises(ValueError):
        factorielle(-1)

@pytest.mark.parametrize("valeur, attendu", [
    (2, 2),
    (3, 6),
    (4, 24),
    (6, 720)
])
def test_factorielle_parametrize(valeur, attendu):
    """Test avec plusieurs valeurs."""
    assert factorielle(valeur) == attendu
```

---

## **4. Exécution des Tests**

Une fois votre test écrit, exécutez-le avec la commande :

```sh
pytest test_maths.py -v
```

Si tous les tests passent, vous devriez voir un résultat comme :

```
======================= test session starts =======================
collected 3 items

test_maths.py ...                                          [100%]

======================= 3 passed in 0.12s ========================
```

Si une erreur est détectée, analysez le message d'erreur et corrigez votre code.

---

## **5. Améliorations Possibles**

- Ajouter un test avec des **valeurs très grandes** (`factorielle(50)`).
- Tester avec **des entrées non valides** (`None`, `"texte"`, `3.5`).
- Vérifier que l’implémentation de `factorielle()` est **optimisée et ne dépasse pas la limite de récursion de Python**.



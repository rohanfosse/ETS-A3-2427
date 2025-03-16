# **Guide d'Utilisation de Pytest**

## **Introduction**

Pytest est une bibliothèque de tests pour Python qui permet de **vérifier automatiquement** le bon fonctionnement de votre code.  
Il est plus puissant et plus simple à utiliser que `unittest`, et permet d'écrire des tests de manière plus concise.

Ce guide présente les bases de Pytest, comment écrire des tests et les exécuter efficacement.

---

## **1. Installation de Pytest**

Avant d'utiliser Pytest, il faut l'installer. Il est recommandé de le faire dans un **environnement virtuel**.

```sh
pip install pytest
```

Vérifiez que l'installation a réussi en affichant la version installée :

```sh
pytest --version
```

---

## **2. Structure d’un Test avec Pytest**

Un test est une fonction qui **vérifie qu'une fonction retourne le bon résultat**.

### **Exemple simple**

#### **Fichier principal (`calculs.py`)**

```python
def addition(a, b):
    return a + b
```

#### **Fichier de test (`test_calculs.py`)**

```python
from calculs import addition

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
```

Ici, `assert` vérifie que le résultat retourné par `addition()` est bien celui attendu.

---

## **3. Exécuter les Tests**

Pour exécuter les tests, tapez simplement :

```sh
pytest
```

Si les tests réussissent, Pytest affichera :

```
======================= test session starts =======================
collected 1 item

test_calculs.py .                                          [100%]

======================= 1 passed in 0.12s ========================
```

Si un test échoue, Pytest affiche l'erreur :

```
======================= test session starts =======================
collected 1 item

test_calculs.py F                                          [100%]

======================= FAILURES ========================
test_addition
    assert addition(2, 3) == 6
    AssertionError: assert 5 == 6
```

Cela montre que la valeur obtenue (`5`) ne correspond pas à la valeur attendue (`6`).

---

## **4. Tester Plusieurs Cas d’un Coup**

Au lieu d'écrire plusieurs `assert`, Pytest permet de tester plusieurs cas d’un coup avec `@pytest.mark.parametrize`.

```python
import pytest
from calculs import addition

@pytest.mark.parametrize("a, b, resultat_attendu", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (10, -5, 5)
])
def test_addition(a, b, resultat_attendu):
    assert addition(a, b) == resultat_attendu
```

Cela permet d’éviter les répétitions et d’écrire des tests plus compacts.

---

## **5. Tester une Fonction qui Doit Lever une Erreur**

Si une fonction doit **lever une erreur** (`raise Exception`), utilisez `pytest.raises()`.

#### **Fichier principal (`operations.py`)**

```python
def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro interdite")
    return a / b
```

#### **Fichier de test (`test_operations.py`)**

```python
import pytest
from operations import division

def test_division():
    assert division(10, 2) == 5
    assert division(9, 3) == 3
    
    with pytest.raises(ValueError):
        division(10, 0)  # Doit lever une erreur
```

Le test **réussit** si l’exception `ValueError` est bien levée lors d’une division par zéro.

---

## **6. Tester une Fonction qui Utilise `input()`**

Si votre fonction demande une **entrée utilisateur** avec `input()`, utilisez `monkeypatch` pour simuler l’entrée.

#### **Fichier principal (`interaction.py`)**

```python
def demander_nom():
    return input("Entrez votre nom : ")
```

#### **Fichier de test (`test_interaction.py`)**

```python
def test_demander_nom(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Alice")
    assert demander_nom() == "Alice"
```

Ici, `monkeypatch.setattr()` **remplace temporairement `input()`** pour tester la fonction **sans intervention humaine**.

---

## **7. Organiser ses Tests avec des Classes**

Vous pouvez regrouper vos tests dans une classe pour mieux organiser votre code.

```python
from calculs import addition

class TestCalculs:
    def test_addition_positive(self):
        assert addition(2, 3) == 5

    def test_addition_negatif(self):
        assert addition(-1, -1) == -2
```

Note : Il ne faut **pas** mettre `self` dans les méthodes, car **Pytest ne nécessite pas d’objets instanciés**.

---

## **8. Exécuter un Test Spécifique**

Si vous avez plusieurs fichiers de tests et que vous voulez exécuter **un seul fichier**, utilisez :

```sh
pytest test_operations.py
```

Pour tester **une seule fonction**, utilisez `-k` suivi du nom du test :

```sh
pytest -k "test_division"
```

Pour afficher **plus de détails** :

```sh
pytest -v
```

---

## **9. Ignorer Certains Tests**

Si vous voulez ignorer un test temporairement, ajoutez `@pytest.mark.skip`.

```python
import pytest

@pytest.mark.skip(reason="En cours de modification")
def test_fonction_non_finie():
    assert 1 + 1 == 3
```

Pour exécuter uniquement **certains tests**, utilisez `@pytest.mark.xfail`.

```python
@pytest.mark.xfail
def test_bug_connu():
    assert 2 * 2 == 5  # Ce test est censé échouer
```

---

## **10. Générer un Rapport de Test**

Pytest permet de générer un **rapport de test détaillé** au format **HTML** :

```sh
pytest --html=rapport_tests.html
```

Vous pouvez ensuite ouvrir `rapport_tests.html` dans un navigateur pour voir les résultats détaillés.

---

## **11. Résumé des Commandes Pytest**

| Commande | Description |
|----------|------------|
| `pytest` | Exécute tous les tests du projet. |
| `pytest test_operations.py` | Exécute uniquement le fichier `test_operations.py`. |
| `pytest -k "test_division"` | Exécute uniquement les tests contenant `test_division`. |
| `pytest -v` | Affiche des détails sur chaque test exécuté. |
| `pytest --maxfail=1` | Arrête après le premier test échoué. |
| `pytest --disable-warnings` | Masque les avertissements. |
| `pytest --html=rapport_tests.html` | Génère un rapport HTML des tests. |

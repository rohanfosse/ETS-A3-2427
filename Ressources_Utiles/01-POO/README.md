# **Programmation Orientée Objet en Python : Concepts Avancés**

## **1. Introduction à la POO en Python**

La **Programmation Orientée Objet (POO)** est un paradigme qui permet de structurer un programme en **objets**, qui sont des instances de **classes**.

### **Pourquoi utiliser la POO en Python ?**

- **Organisation du code** : Facilite la réutilisation et la maintenance.
- **Encapsulation des données** : Contrôle l'accès aux informations.
- **Héritage** : Permet la réutilisation du code.
- **Polymorphisme** : Offre de la flexibilité dans l'utilisation des classes.

### **Définition d’une classe et d’un objet**

En Python, tout est objet, y compris les nombres, les chaînes de caractères et les fonctions.

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans."

# Création d'une instance
p = Personne("Alice", 30)
print(p.se_presenter())
```

Ce rappel étant fait, passons aux concepts avancés.

---

## **2. Encapsulation et Attributs Privés**

L’**encapsulation** permet de restreindre l'accès à certaines données et de les protéger contre des modifications non voulues.

### **Attributs privés et protégés**

- `_attribut_protégé` : Convention indiquant que cet attribut ne doit pas être modifié directement.
- `__attribut_privé` : Rend l’attribut **inaccessible en dehors de la classe**.

```python
class CompteBancaire:
    def __init__(self, solde):
        self.__solde = solde  # Attribut privé

    def deposer(self, montant):
        self.__solde += montant

    def retirer(self, montant):
        if montant <= self.__solde:
            self.__solde -= montant
        else:
            print("Fonds insuffisants.")

    def afficher_solde(self):
        return f"Solde : {self.__solde}€"

compte = CompteBancaire(100)
compte.deposer(50)
compte.retirer(30)
print(compte.afficher_solde())
```

🔹 **Accéder à un attribut privé** se fait via une méthode publique (`afficher_solde()`).

---

## **3. Propriétés et Méthodes Getter/Setter**

Les **propriétés** permettent de gérer l’accès aux attributs de manière contrôlée.

### **Utilisation de `@property`**

```python
class Employe:
    def __init__(self, nom, salaire):
        self.nom = nom
        self.__salaire = salaire

    @property
    def salaire(self):
        """Getter : retourne le salaire"""
        return self.__salaire

    @salaire.setter
    def salaire(self, montant):
        """Setter : modifie le salaire uniquement si positif"""
        if montant >= 0:
            self.__salaire = montant
        else:
            raise ValueError("Le salaire ne peut pas être négatif.")

e = Employe("Alice", 3000)
print(e.salaire)  # Accès via le getter
e.salaire = 3500  # Modification via le setter
```

🔹 `@property` évite d’utiliser des méthodes explicites comme `get_salaire()` et `set_salaire()`.

---

## **4. Héritage et Héritage Multiple**

L’**héritage** permet de créer une nouvelle classe basée sur une classe existante.

### **Héritage Simple**

```python
class Animal:
    def parler(self):
        raise NotImplementedError("Cette méthode doit être implémentée")

class Chien(Animal):
    def parler(self):
        return "Wouf !"

class Chat(Animal):
    def parler(self):
        return "Miaou !"

animaux = [Chien(), Chat()]
for animal in animaux:
    print(animal.parler())  # Polymorphisme
```

### **Héritage Multiple**

Python permet l’héritage de **plusieurs classes en même temps**.

```python
class A:
    def afficher(self):
        return "Classe A"

class B:
    def afficher(self):
        return "Classe B"

class C(A, B):  # Hérite de A et B
    pass

c = C()
print(c.afficher())  # Affichera "Classe A" (ordre de résolution des méthodes)
```

🔹 **L’ordre de résolution des méthodes (MRO)** est déterminé par l’algorithme **C3 linearization**.

---

## **5. Polymorphisme et Méthodes Magiques**

Le **polymorphisme** permet d’utiliser une interface commune pour des objets différents.

### **Méthodes Magiques (`__str__`, `__repr__`, `__eq__`, etc.)**

Python propose des **méthodes spéciales**, appelées aussi **méthodes magiques**, permettant de personnaliser le comportement des objets.

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"{self.nom}, {self.age} ans"

p = Personne("Alice", 30)
print(p)  # Appelle __str__()
```

🔹 **Méthodes magiques utiles** :

- `__str__` : Représentation en tant que chaîne de caractères.
- `__repr__` : Représentation officielle (pour le debugging).
- `__eq__` : Comparaison d’objets (`==`).
- `__call__` : Rendre un objet **appelable comme une fonction**.

---

## **6. Composition vs Héritage**

Plutôt que d’utiliser l’héritage, **la composition** permet d’assembler des objets.

```python
class Moteur:
    def demarrer(self):
        return "Moteur en marche"

class Voiture:
    def __init__(self):
        self.moteur = Moteur()  # Composition

    def demarrer(self):
        return self.moteur.demarrer()

v = Voiture()
print(v.demarrer())  # "Moteur en marche"
```

🔹 **Règle générale** :  
➡ **Héritage** = "est un" (`Chien` **est un** `Animal`).  
➡ **Composition** = "a un" (`Voiture` **a un** `Moteur`).

---

## **7. Interfaces et Classes Abstraites**

Les **interfaces** définissent un contrat que les classes doivent respecter.

### **Classes Abstraites en Python**

Python n’a pas d’interfaces explicites, mais utilise `ABC` (Abstract Base Class).

```python
from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return 3.14 * self.rayon ** 2

c = Cercle(10)
print(c.aire())  # OK
```

🔹 **Avantage** : Force les classes enfants à implémenter certaines méthodes.

---

## **8. Design Patterns en POO**

Les **Design Patterns** sont des modèles de conception réutilisables.

### **Pattern Singleton**

Permet d’avoir **une seule instance** d’une classe.

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### **Pattern Factory**

Permet de **créer des objets sans exposer leur implémentation**.

```python
class Factory:
    @staticmethod
    def creer_animal(type_animal):
        if type_animal == "chien":
            return Chien()
        elif type_animal == "chat":
            return Chat()
        else:
            raise ValueError("Type inconnu")
```

---

---
**Pour aller plus loin** : [Documentation POO Python](https://docs.python.org/3/tutorial/classes.html)

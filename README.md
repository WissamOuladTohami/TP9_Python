### Mini-Projet :

Ce mini-projet a pour objectif de mettre en pratique la **programmation orientée objet (POO)** en Python ainsi que l’**accès aux bases de données**, en comparant l’utilisation d’une base **SQLite** (embarquée) et d’une base **MySQL** (distante).

Le projet consiste à gérer des **entités métiers** simples (`Produit` et `Client`) à l’aide de classes Python, puis à implémenter les opérations CRUD (création, lecture, recherche, mise à jour) à travers deux implémentations distinctes (SQLite et MySQL) partageant la **même interface logicielle**.  
Cela permet de comprendre comment adapter un code Python à différents systèmes de gestion de bases de données tout en conservant une architecture propre et maintenable.

---

### Fonctionnalités

- **Modélisation orientée objet**
  - Classe `Produit` avec les attributs : `id`, `nom`, `prix`
  - Classe `Client` avec les attributs : `id`, `nom`, `email`
  - Méthode `__str__()` pour un affichage lisible des objets

- **Gestion des bases de données**
  - Base SQLite locale : `boutique.db`
  - Base MySQL distante : `boutique`
  - Création automatique des tables `produits` et `clients`

- **Opérations CRUD**
  - Ajouter un produit ou un client
  - Lister tous les produits ou tous les clients
  - Rechercher un client par adresse email
  - Modifier le prix d’un produit existant

- **DAO avec interface commune**
  - Module `sqlite_dao.py` pour SQLite
  - Module `mysql_dao.py` pour MySQL
  - Méthodes identiques dans les deux modules (ex. `ajouter_produit()`, `lister_clients()`)
  - Possibilité de remplacer facilement le type de base sans modifier le reste du code

- **Menu interactif (CLI)**
  - Fichier `main.py` proposant un menu en ligne de commande
  - Tests des fonctionnalités CRUD via SQLite ou MySQL
  - Affichage clair des résultats et des messages d’erreur

- **Gestion des erreurs**
  - Détection des erreurs de connexion à la base
  - Gestion des erreurs SQL
  - Messages explicites pour guider l’utilisateur

---

### Résultats / Captures d’écran

#### Exemple de sortie du menu CLI

```text
1. Ajouter un produit
2. Lister les produits
3. Ajouter un client
4. Lister les clients
5. Rechercher un client par email
6. Modifier le prix d’un produit
0. Quitter
```

Exemple d’affichage (Ajout & liste des produits) :

<img width="1154" height="546" alt="1   2" src="https://github.com/user-attachments/assets/e818bcc6-c9a3-43df-888a-90e98dc0a483" />



Exemple d'affichage (modification & liste des produits) :

<img width="858" height="446" alt="3" src="https://github.com/user-attachments/assets/56471798-392b-455f-9b47-24d2987fe9b5" />



Exemple d'affichage (Ajout & liste des clients & Recherche par email) :

<img width="796" height="596" alt="4   5   6" src="https://github.com/user-attachments/assets/b5ab5273-a49f-41ae-9658-096db1ef1516" />

(Produits) Au niveau de la base de données :

<img width="458" height="71" alt="BD1" src="https://github.com/user-attachments/assets/0c1e04a9-cffd-4472-a509-adf7ef427d0e" />

(Clients) Au niveau de la base de données :

<img width="574" height="69" alt="BD2" src="https://github.com/user-attachments/assets/d84b625d-de25-4d03-911e-f370da3f139b" />





from models import Produit, Client
from sqlite_dao import SQLiteDAO
from mysql_dao import MySQLDAO
from base_dao import BoutiqueDAO


def choisir_impl() -> BoutiqueDAO:
    """
    Permet à l'utilisateur de choisir entre SQLite et MySQL.
    Retourne un objet qui implémente BoutiqueDAO.
    """
    while True:
        print("=== Choix de la base de données ===")
        print("1. SQLite (boutique.db)")
        print("2. MySQL (base 'boutique')")
        choix = input("Votre choix (1/2) : ").strip()

        if choix == "1":
            return SQLiteDAO()
        elif choix == "2":
            try:
                return MySQLDAO()
            except Exception:
                print("Impossible de se connecter à MySQL. Vérifiez la configuration.")
        else:
            print("Choix invalide.\n")


def afficher_menu():
    print("\n=== Menu principal ===")
    print("1. Ajouter un produit")
    print("2. Lister tous les produits")
    print("3. Modifier le prix d’un produit")
    print("4. Ajouter un client")
    print("5. Lister tous les clients")
    print("6. Rechercher un client par email")
    print("0. Quitter")


def main():
    dao: BoutiqueDAO = choisir_impl()

    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            nom = input("Nom du produit : ")
            prix_str = input("Prix du produit : ")
            try:
                prix = float(prix_str)
                produit = Produit(id_=None, nom=nom, prix=prix)
                dao.ajouter_produit(produit)
                print("Produit ajouté avec succès.")
            except ValueError:
                print("Prix invalide.")

        elif choix == "2":
            produits = dao.lister_produits()
            if not produits:
                print("Aucun produit trouvé.")
            else:
                print("Liste des produits :")
                for p in produits:
                    print("  -", p)

        elif choix == "3":
            id_str = input("ID du produit : ")
            nouveau_prix_str = input("Nouveau prix : ")
            try:
                id_produit = int(id_str)
                nouveau_prix = float(nouveau_prix_str)
                modifie = dao.modifier_prix_produit(id_produit, nouveau_prix)
                if modifie:
                    print("Prix modifié avec succès.")
                else:
                    print("Aucun produit avec cet ID.")
            except ValueError:
                print("ID ou prix invalide.")

        elif choix == "4":
            nom = input("Nom du client : ")
            email = input("Email du client : ")
            client = Client(id_=None, nom=nom, email=email)
            dao.ajouter_client(client)
            print("Client ajouté (ou tentative) terminée.")

        elif choix == "5":
            clients = dao.lister_clients()
            if not clients:
                print("Aucun client trouvé.")
            else:
                print("Liste des clients :")
                for c in clients:
                    print("  -", c)

        elif choix == "6":
            email = input("Email du client à rechercher : ")
            client = dao.rechercher_client_par_email(email)
            if client:
                print("Client trouvé :", client)
            else:
                print("Aucun client avec cet email.")

        elif choix == "0":
            print("Fermeture de la connexion et arrêt du programme.")
            dao.close()
            break

        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()

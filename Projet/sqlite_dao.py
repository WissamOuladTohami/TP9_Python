import sqlite3
from typing import Optional
from models import Produit, Client
from base_dao import BoutiqueDAO


class SQLiteDAO(BoutiqueDAO):
    def __init__(self, chemin_db: str = "boutique.db"):
        try:
            self.conn = sqlite3.connect(chemin_db)
            self.conn.row_factory = sqlite3.Row  
            self._creer_tables()
        except sqlite3.Error as e:
            print(f"Erreur de connexion SQLite : {e}")
            raise

    def _creer_tables(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS produit (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prix REAL NOT NULL
            )
            """
        )
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS client (id INTEGER PRIMARY KEY AUTOINCREMENT,nom TEXT NOT NULL,email TEXT UNIQUE NOT NULL)"""
        )
        self.conn.commit()


    def ajouter_produit(self, produit: Produit) -> None:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO produit (nom, prix) VALUES (?, ?)",
                (produit.nom, produit.prix),
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erreur lors de l'ajout du produit : {e}")

    def lister_produits(self) -> list[Produit]:
        produits: list[Produit] = []
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id, nom, prix FROM produit")
            for row in cursor.fetchall():
                produits.append(
                    Produit(
                        id_=row["id"],
                        nom=row["nom"],
                        prix=row["prix"],
                    )
                )
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des produits : {e}")
        return produits

    def modifier_prix_produit(self, id_produit: int, nouveau_prix: float) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE produit SET prix = ? WHERE id = ?",
                (nouveau_prix, id_produit),
            )
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Erreur lors de la modification du prix : {e}")
            return False


    def ajouter_client(self, client: Client) -> None:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO client (nom, email) VALUES (?, ?)",
                (client.nom, client.email),
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Erreur : un client avec cet email existe déjà.")
        except sqlite3.Error as e:
            print(f"Erreur lors de l'ajout du client : {e}")

    def lister_clients(self) -> list[Client]:
        clients: list[Client] = []
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id, nom, email FROM client")
            for row in cursor.fetchall():
                clients.append(
                    Client(
                        id_=row["id"],
                        nom=row["nom"],
                        email=row["email"],
                    )
                )
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des clients : {e}")
        return clients

    def rechercher_client_par_email(self, email: str) -> Optional[Client]:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT id, nom, email FROM client WHERE email = ?",
                (email,),
            )
            row = cursor.fetchone()
            if row:
                return Client(id_=row["id"], nom=row["nom"], email=row["email"])
            return None
        except sqlite3.Error as e:
            print(f"Erreur lors de la recherche du client : {e}")
            return None


    def close(self) -> None:
        if self.conn:
            self.conn.close()

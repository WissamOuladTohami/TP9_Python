from typing import Optional
import mysql.connector
from mysql.connector import Error
from models import Produit, Client
from base_dao import BoutiqueDAO
from config import MYSQL_CONFIG


class MySQLDAO(BoutiqueDAO):
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host=MYSQL_CONFIG["host"],
                user=MYSQL_CONFIG["user"],
                password=MYSQL_CONFIG["password"],
                database=MYSQL_CONFIG["database"],
            )
            if not self.conn.is_connected():
                raise Error("Connexion MySQL échouée")
            self._creer_tables()
        except Error as e:
            print(f"Erreur de connexion MySQL : {e}")
            raise

    def _creer_tables(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS produit (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255) NOT NULL,
                prix DOUBLE NOT NULL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS client (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE
            )
            """
        )
        self.conn.commit()
        cursor.close()

    #
    def ajouter_produit(self, produit: Produit):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO produit (nom, prix) VALUES (%s, %s)",
                (produit.nom, produit.prix),
            )
            self.conn.commit()
        except Error as e:
            print(f"Erreur lors de l'ajout du produit : {e}")
        finally:
            cursor.close()

    def lister_produits(self):
        produits: list[Produit] = []
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT id, nom, prix FROM produit")
            for row in cursor.fetchall():
                produits.append(
                    Produit(
                        id_=row["id"],
                        nom=row["nom"],
                        prix=row["prix"],
                    )
                )
        except Error as e:
            print(f"Erreur lors de la récupération des produits : {e}")
        finally:
            cursor.close()
        return produits

    def modifier_prix_produit(self, id_produit: int, nouveau_prix: float):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE produit SET prix = %s WHERE id = %s",
                (nouveau_prix, id_produit),
            )
            self.conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Erreur lors de la modification du prix : {e}")
            return False
        finally:
            cursor.close()

    
    def ajouter_client(self, client: Client):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO client (nom, email) VALUES (%s, %s)",
                (client.nom, client.email),
            )
            self.conn.commit()
        except Error as e:
            
            if e.errno == 1062:
                print("Erreur : un client avec cet email existe déjà.")
            else:
                print(f"Erreur lors de l'ajout du client : {e}")
        finally:
            cursor.close()

    def lister_clients(self):
        clients: list[Client] = []
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT id, nom, email FROM client")
            for row in cursor.fetchall():
                clients.append(
                    Client(
                        id_=row["id"],
                        nom=row["nom"],
                        email=row["email"],
                    )
                )
        except Error as e:
            print(f"Erreur lors de la récupération des clients : {e}")
        finally:
            cursor.close()
        return clients

    def rechercher_client_par_email(self, email: str):
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT id, nom, email FROM client WHERE email = %s",
                (email,),
            )
            row = cursor.fetchone()
            if row:
                return Client(
                    id_=row["id"],
                    nom=row["nom"],
                    email=row["email"],
                )
            return None
        except Error as e:
            print(f"Erreur lors de la recherche du client : {e}")
            return None
        finally:
            cursor.close()

    
    def close(self) -> None:
        if self.conn and self.conn.is_connected():
            self.conn.close()

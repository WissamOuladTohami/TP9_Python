class Produit:
    def __init__(self, id_: int, nom: str, prix: float):
        self.id = id_
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"Produit(id={self.id}, nom='{self.nom}', prix={self.prix})"


class Client:
    def __init__(self, id_: int, nom: str, email: str):
        self.id = id_
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"Client(id={self.id}, nom='{self.nom}', email='{self.email}')"
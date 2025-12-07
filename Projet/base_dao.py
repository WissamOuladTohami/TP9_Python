from abc import ABC, abstractmethod
from models import Produit, Client


class BoutiqueDAO(ABC):
  
    @abstractmethod
    def ajouter_produit(self, produit: Produit):
        pass

    @abstractmethod
    def ajouter_client(self, client: Client):
        pass

    @abstractmethod
    def lister_produits(self):
        pass

    @abstractmethod
    def lister_clients(self):
        pass

    @abstractmethod
    def rechercher_client_par_email(self, email: str):
        pass

    @abstractmethod
    def modifier_prix_produit(self, id_produit: int, nouveau_prix: float):
        pass

    @abstractmethod
    def close(self) -> None:
        pass
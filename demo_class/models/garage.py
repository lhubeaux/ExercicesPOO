from .voiture import Voiture

class Garage:
    
    def ajouter_voiture(self, voiture : Voiture):
        if not hasattr(self, 'voitures'):
            self.voitures = [] #on ajoute la liste ici pour qu'elle soit propre à l'instance du garage
            self.nombre_voitures = 0
            self.nom = "Mon garage"
        
        self.voitures.append(voiture)
        self.nombre_voitures += 1
        return f"{voiture} ajoutée à {self.nom}"
    
    def supprimer_voiture(self):
        pass

    def afficher_toutes_voitures(self):
        if not hasattr(self, 'voitures') or not self.voitures:
            return f"{self.nom} est vide !"
        
        resultat = f"Garage {getattr(self, 'nom', 'Sans nom')} - {self.nombre_voitures} voiture(s)\n"
        resultat += "=" * 50 + "\n"

        for voiture in self.voitures:
            resultat += voiture.afficher_info() + "\n\n"

        return resultat
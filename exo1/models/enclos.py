from .elephant import Elephant

class Enclos:
    
    def definir_enclos(self, nom, capacite_max, taille):
        self.nom = nom
        self.capacite_max = capacite_max
        self.taille = taille
        self.liste_animaux = []

    def ajouter_animal(self, animal : Elephant):
        self.liste_animaux.append(animal)
        return f"{self.nom} contient désormais {animal.nom}"
    
    def retirer_animal(self, animal : Elephant):
        self.liste_animaux.pop(animal)
        return f"{animal.nom} n'est plus dans {self.nom}"
    
    def afficher_animaux(self):
        if not hasattr(self, "liste_animaux"):
            return "L'enclos est vide!"
        
        resultat = f"{self.nom} contient {len(self.liste_animaux)} animal/animaux: \n"
        resultat += "=" * 50 + "\n"

        for animal in self.liste_animaux:
            resultat += animal.afficher_elephant() + "\n\n"
        
        return resultat
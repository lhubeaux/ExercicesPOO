from .elephant import Elephant

class Soigneur:

    def definir_soigneur(self, nom, date_naissance, experience):
        self.nom = nom
        self.date_naissance = date_naissance
        self.experience = experience
        self.nombre_animaux_responsable = 0
    
    def ajouter_animal(self, animal : Elephant):
        self.animaux = []
        self.nombre_animaux_responsable += 1
        self.animaux.append(animal)
        return f"{self.nom} est responsable de {animal.nom}"



    def nourrir(self, animal : Elephant):
        if not hasattr(self, "animaux"):
             return "Ce soigneur n'est responsable d'aucun animal!"
        else:
            animal.appetit = 100
        return f"{animal.nom} est rassasié!"

    def entretenir(self, animal : Elephant):
        if not hasattr(self, "animaux"):
             return "Ce soigneur n'est responsable d'aucun animal!"
        else:
            animal.satisfaction = 100
        return f"{animal.nom} est content!"
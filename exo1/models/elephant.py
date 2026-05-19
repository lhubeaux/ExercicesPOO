from .soigneur import Soigneur

class Elephant:
    
    def definir_elephant(self, nom, appetit, satisfaction, soigneur):
        self.nom = nom
        self.appetit = appetit
        self.satisfaction = satisfaction
        self.en_vie = True
        self.soigneur = soigneur


    def manger(self):
        self.appetit = 100

    def afficher_elephant(self):
        if not hasattr(self, 'appetit'):
            return f"Cet éléphant n'a pas été encodé"
        return f"{self.nom} a un appétit de {self.appetit} et une satisfaction de {self.satisfaction}, son soigneur est {self.soigneur}."
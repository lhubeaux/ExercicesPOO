from models import Voiture, Electrique


class VoitureElectrique(Voiture, Electrique):
    def definir(self, marque, modele, annee, couleur, kilometrage, autonomie):
        super().definir(marque, modele, annee, couleur, kilometrage)
        Electrique.definir(self, autonomie)
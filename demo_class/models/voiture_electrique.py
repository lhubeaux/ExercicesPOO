from .electrique import Electrique
from .voiture import Voiture

class VoitureElectrique(Voiture, Electrique):

    def definir(self, marque, modele, annee, couleur, kilometrage, autonomie):
        super().definir(marque, modele, annee, couleur, kilometrage)
        #On aurait aussi pu mettre voiture().definir()
        Electrique.definir(self, autonomie)
    
    def demarrer(self):
        
        resultat = "Voiture electrique : \n "
        resultat += "-> Mode silencieux \n"
        resultat += super().demarrer() + "\n"
        return resultat
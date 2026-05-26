from .animal import Animal

class Giraffe(Animal):

    #region Attributs

    def __init__(self, nom, appetit=50, satisfaction=50, en_vie=True, soigneur=None, longueur_cou=250):
        super().__init__(nom, appetit, satisfaction, en_vie, soigneur)
        self.__longueur_cou = max(0, min(300, longueur_cou))
        # return f"Giraffe {nom} créée.\n Appétit : {appetit}/100\n {satisfaction}/100\n Son soigneur est {soigneur}"

    #endregion

    #region Prop's

    @property
    def longueur_cou(self):
        return self.__longueur_cou
    
    # @longueur_cou.setter
    # def longueur_cou(self, value):
    #     if not isinstance(value, int):
    #         raise TypeError("La longueur du coup doit être un nombre entier positif")
    #     if value < 1:
    #         raise ValueError("La longueur du coup doit être un nombre entier positif de minimum 1 cm")
    #     self.__longueur_cou = value


    #endregion

    #region Methodes

    def manger_feuilles(self):
        if not hasattr(self, 'nom') or not self.en_vie:
            return "[Erreur] Giraffe non définie ou morte..."
        self.appetit += 10
        self.satisfaction += 10
        return f"{self.nom} mange des feuilles 🌿"

    def boire_eau(self):
        if not hasattr(self, 'nom') or not self.en_vie:
            return "[Erreur] Giraffe non définie ou morte..."
        self.__satisfaction = min(100, self.satisfaction + 20)
        return f"{self.nom} boit de l'eau."
    
    def observer_environnements(self):
	    return f"{self.nom} regarde son environnement du haut de son cou"
    #endregion
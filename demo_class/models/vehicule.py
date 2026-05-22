class Vehicule():
    """

Classe parent  : Tous les types de véhicules

    """

#region Attributs
    def definir(self, marque, modele, annee):
            """
            Méthode pour initialiser les attributs (remplace le constructeur)
            """
            self.marque = marque
            self.modele = modele
            self.annee = annee
            return f"Véhicule {marque} {modele} défini"
#endregion

#region Methodes
    def afficher_info(self):
          return (f"{self.marque} {self.modele} ({self.annee})")
    def demarrer(self):
          return (f"{self.marque} {self.modele} demarre normalement")
#endregion
class Voiture:
    """
    Classe Voiture:
    """
    #region Attributs
    nombre_voitures = 0  #Attribut de classe

    #endregion
    
    #region Propriétés

    @property
    def couleur(self): 
        """
        getter qui lit la couleur
        """
        return self._couleur

#si on ne met pas de setter, on ne peut plus changer la couleur

    @couleur.setter
    def couleur(self, nouvelle_couleur):
        if not isinstance(nouvelle_couleur, str): #Si la couleur n'est pas un string alors on aura une erreur
            raise TypeError("La couleur doit être du texte")
        self._couleur = nouvelle_couleur.capitalize()

    #endregion


    #region Methodes
    def definir_voiture(self, marque, modele, couleur, annee, kilometrage):
        """
        Méthode pour initialiser les attributs (remplace le constructeur)
        """
        self.marque = marque
        self.modele = modele
        self._couleur = couleur #On passe la couleur en privé
        self.anne = annee
        self.kilometrage = kilometrage
        self.est_demarre = False

        Voiture.nombre_voitures += 1
        print(f"Nombre de de voitures : {self.nombre_voitures}")
    
    def demarrer(self):
        if not hasattr(self, 'est_demarre'):
            return "[Erreur] Veuillez d'abord définir la voiture avec definir_voiture"
        if not self.est_demarre:
            self.est_demarre = True
            return f"[Succès] {self.marque} {self.modele} a démarré, vroum skrrt"
        return f"[Succès] {self.marque} {self.modele} a déjà démarré"
    
    def arreter(self):
        pass
    
    def rouler(self):
        pass
    
    def afficher_info(self):
        if not hasattr(self, 'marque'):
            return "Voiture non définie"
        return f"🚗 {self.marque} {self.modele}"

    def __str__(self):
        if hasattr(self, 'marque'):
            return f"{self.marque}"
        return "Voiture (non définie)"
    #endregion
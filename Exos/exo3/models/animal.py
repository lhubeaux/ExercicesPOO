class Animal:


#region attribut
    def definir(self, nom, appetit=50, satisfaction=50, en_vie=True, soigneur=None):
        self.__nom = nom
        self.__appetit = max(0, min(100, appetit))
        self.__satisfaction = max(0, min(100, satisfaction))
        self.__en_vie = en_vie
        self.__soigneur = soigneur
#endregion

#region Prop's

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        if not isinstance(value, str):
            raise TypeError("Le mot doit être une chaine")
        self.__nom = value

    @property
    def appetit(self):
        return self.__appetit

    @property
    def satisfaction(self):
        return self.__satisfaction

    @property
    def en_vie(self):
        return self.__en_vie

    @property
    def soigneur(self):
        return self.__soigneur

    @soigneur.setter
    def soigneur(self, value):
        self.__soigneur = value

    #endregion

#region methodes
    def observer_environnements(self):
        return f"{self.nom} regarde son environnement et les autres animaux"

#endregion
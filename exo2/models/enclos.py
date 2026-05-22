class Enclos:

	def definir(self, nom, capacite_max, taille):
		self.__nom = nom
		self.__capacite_max = capacite_max
		self.__taille = taille
		self.__liste_animaux = []
		return f"Enclos {nom} créé"
	


	#region properties

	@property
	def nom(self):
		return self.__nom
	
	@nom.setter
	def nom(self, nouveau_nom):
		if not isinstance(nouveau_nom, str): 
			raise TypeError("Le nom doit être du texte")
		self.__nom = nouveau_nom.capitalize()

	@property
	def capacite_max(self):
		return self.__capacite_max
	
	@nom.setter
	def capacite_max(self, value):
		if not isinstance(value, int) or value < 1: 
			raise TypeError("La valeur doit être un nombre entier positif")
		self.__capacite_max = value

	@property
	def taille(self):
		return self.__taille
	
	@property
	def liste_animaix(self):
		return self.__liste_animaux
	


	#endregion

# en n'ajoutant pas les __ aux noms des attributs on appelle la variable et on se complique donc la vie --> mieux de les rajouter
	def ajouter_animal(self,animal):
		if not hasattr(self, 'liste_animaux'):
			self.liste_animaux = []

		if len(self.liste_animaux) >= self.capacite_max:
			return f"Capacité max atteinte ({self.capacite_max})"

		self.liste_animaux.append(animal)
		return f"{animal.nom} ajouté à {self.nom}"

	def enleve_animal(self, animal):
		if animal in self.liste_animaux:
			self.liste_animaux.remove(animal)
			return f"{animal.nom} retiré de l'enclos"
		return "Animal non présent"

	def aficher_animaux(self):
		if not hasattr(self, 'liste_animaux') or not self.liste_animaux:
			return f"L'enclos {self.nom} est vide"

		resultat = f"Enclos {self.nom} ({len(self.liste_animaux)}/{self.capacite_max})\n"
		resultat += "=" * 50 + "\n"
		for animal in self.liste_animaux:
			resultat += animal.afficher_etat() + "\n\n"
		return resultat

	def passer_jour(self):
		"""
		Simule le passage d'une journée
		"""
		if not hasattr(self, 'liste_animaux') or not self.liste_animaux:
			return f"L'enclos {self.nom} est vide"

		resultat = f"\n 🌄 Passage d'une journée dans {self.nom} 🌄\n"
		resultat += '-' * 42 + "\n"

		for animal in self.liste_animaux:
			if animal.en_vie:
				animal.appetit = min(100, animal.appetit + 35)
				animal.satisfaction = max(0, animal.satisfaction - 25)

				resultat += f"{animal.nom} => Appétit = {animal.appetit}/100 | Satisfaction : {animal.satisfaction}/100\n"

				if animal.appetit >= 95 or animal.satisfaction <= 5:
					animal.en_vie = False
					resultat += f"😵 {animal.nom} est tombé malade ou est mort...\n"
			else:
				resultat += f"{animal.nom} est déjà mort\n"
    
		resultat += '-' * 42 + "\n"
		return resultat

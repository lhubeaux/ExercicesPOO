class Enclos:

	#region Attributs

	def definir(self, nom, capacite_max, taille):
		self.__nom = nom
		self.__capacite_max = capacite_max
		self.__taille = taille
		self.__liste_animaux = []
		return f"Enclos {nom} créé"

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
	def capacite_max(self):
		return self.__capacite_max

	@capacite_max.setter
	def capacite_max(self, value):
		if not isinstance(value, int) or value < 1:
			raise TypeError("La capacité max doit être un entier positif")
		self.__capacite_max = value

	@property
	def taille(self):
		return self.__taille

	@property
	def liste_animaux(self):
		return self.__liste_animaux

	#endregion

	#region Methodes

	def ajouter_animal(self,animal):
		if not hasattr(self, 'liste_animaux'):
			self.__liste_animaux = []

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
				animal.passe_le_temps()

				resultat += f"{animal.nom} => Appétit = {animal.appetit}/100 | Satisfaction : {animal.satisfaction}/100\n"

				if animal.appetit >= 95 or animal.satisfaction <= 5:
					resultat += animal.decede()
			else:
				resultat += f"{animal.nom} est déjà mort\n"
    
		resultat += '-' * 42 + "\n"
		return resultat

	#endregion

class Elephant:

#region attributs
	def definir(self, nom, appetit=50, satisfaction=50, en_vie=True, soigneur=None):
		self.__nom = nom
		self.__appetit = max(0, min(100, appetit))
		self.__satisfaction = max(0, min(100, satisfaction))
		self.__en_vie = en_vie
		self.__soigneur = soigneur
		return f"Éléphant {nom} créé"
#endregion


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
	def soigneur(self, nouveau_soigneur):
		if not isinstance(nouveau_soigneur, str):
			raise TypeError("Le nom du nouveau soigneur doit être en lettres")
		self.__soigneur = nouveau_soigneur.capitalize()

	#endregion


#region methodes

	def manger(self):
		if not hasattr(self, 'nom') or not self.en_vie:
			return "[Erreur] Éléphant non défini ou mort..."

		self.appetit = max(0, self.appetit - 25)
		self.satisfaction = min(100, self.satisfaction + 15)

		return (f"🍉 {self.nom} a mangé. \n"
                    f"    Appétit 		 : {self.appetit}/100\n"
                    f"    Satisfaction   : {self.satisfaction}/100")

	def afficher_etat(self):
		if not hasattr(self, 'nom'):
			return "[Erreur] Éléphant non défini..."
		etat = "Vivant" if self.en_vie else "Mort"
		soigneur_nom = self.soigneur.nom if self.soigneur else "Aucun"

		return (f"🐘 {self.nom}\n"
				f"    Appétit 		 : {self.appetit}/100\n"
				f"    Satisfaction   : {self.satisfaction}/100\n"
				f"    État   		 : {etat}\n"
				f"    Soigneur  	 : {soigneur_nom}")
	
#endregion
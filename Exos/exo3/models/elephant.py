from .animal import Animal
class Elephant(Animal):

	#region Attributs

	def definir(self, nom, appetit=50, satisfaction=50, en_vie=True, soigneur=None, longueur_defense=100):
		super().definir(nom, appetit=50, satisfaction=50, en_vie=True, soigneur=None)
		self.__longueur_defense = max(0, min(300, longueur_defense))
		return f"Giraffe {nom} créée.\n Appétit : {appetit}/100\n {satisfaction}/100\n Son soigneur est {soigneur}"

	#endregion

	#region Prop's


	@property
	def longueur_defense(self):
			return self.__longueur_defense
		
	@longueur_defense.setter
	def longueur_defense(self, value):
			if not isinstance(value, int):
				raise TypeError("La longueur des défenses doit être un nombre entier positif")
			self.__longueur_defense = value

	#endregion

	#region Methodes

	def manger(self):
		if not hasattr(self, 'nom') or not self.en_vie:
			return "[Erreur] Éléphant non défini ou mort..."

		self.__appetit = max(0, self.appetit - 25)
		self.__satisfaction = min(100, self.satisfaction + 15)

		return (f"🍉 {self.nom} a mangé. \n"
                    f"    Appétit 		 : {self.appetit}/100\n"
                    f"    Satisfaction   : {self.satisfaction}/100")

	def laver(self, soigneur=None):
		if not hasattr(self, 'satisfaction') or not self.en_vie:
			return "[Erreur] Éléphant non défini ou mort..."

		if soigneur:
			self.__satisfaction = min(100, self.satisfaction + 30)
			return (f"💧 {self.nom} est lavé par {soigneur.nom} \n"
					f"    Satisfaction   : {self.satisfaction}/100")
		else:
			self.__satisfaction = min(100, self.satisfaction + 15)
			return (f"💦 {self.nom} se lave \n"
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

	def passe_le_temps(self):
		self.__appetit = max(0, self.appetit - 15)
		self.__satisfaction = min(100, self.satisfaction - 25)

	def decede(self):
		self.__en_vie = False
		return f"😵 {self.__nom} est tombé malade ou est mort...\n"
	
	def bain_de_boue(self):
		if not hasattr(self, 'nom') or not self.en_vie:
			return "[Erreur] Elephant non défini ou mort..."
		self.__satisfaction = min(100, self.satisfaction + 10)
		return f"{self.nom} se relaxe dans la boue"

	def baspirer_eau(self):
		if not hasattr(self, 'nom') or not self.en_vie:
			return "[Erreur] Elephant non défini ou mort..."
		self.__satisfaction = min(100, self.satisfaction + 20)
		return f"{self.nom} boit de l'eau"

	def observer_environnements(self):
		return f"{self.nom} regarde son environnement et les autres éléphants"
	#endregion
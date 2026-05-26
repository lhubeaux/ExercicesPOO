from .animal import Animal
class Elephant(Animal):

	#region Attributs

	def __init__(self, nom, appetit=50, satisfaction=50, en_vie=True, soigneur=None, longueur_defense=100):
		super().__init__(nom, appetit, satisfaction, en_vie, soigneur)
		self.__longueur_defense = max(0, min(300, longueur_defense))
		# return f"Elephant {nom} créée.\n Appétit : {appetit}/100\n {satisfaction}/100\n Son soigneur est {soigneur}"

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

	
	
	def bain_de_boue(self):
		if not hasattr(self, 'nom') or not self.en_vie:
			return "[Erreur] Elephant non défini ou mort..."
		self.__satisfaction = min(100, self.satisfaction + 10)
		return f"{self.nom} se relaxe dans la boue"

	def aspirer_eau(self):
		if not hasattr(self, 'nom') or not self.en_vie:
			return "[Erreur] Elephant non défini ou mort..."
		self.__satisfaction = min(100, self.satisfaction + 20)
		return f"{self.nom} boit de l'eau"

	def observer_environnements(self):
		return f"{self.nom} regarde son environnement à travers ses défenses"
	#endregion
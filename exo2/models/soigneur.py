from datetime import date

class Soigneur:

	def definir(self, nom, date_naissance, experience, nombre_animaux_responsable=0):
		self.__nom = nom
		self.__date_naissance = date_naissance
		self.__experience = experience
		self.__nombre_animaux_responsable = nombre_animaux_responsable
		return f"Soigneur {nom} créé"

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
	def date_naissance(self):
		return self.__date_naissance
	
	@property
	def experience(self):
		return self.__experience
	
	@property
	def nombre_animaux_responsable(self):
		return self.__nombre_animaux_responsable
	
	@property
	def age_soigneur(self):
		jour, mois, annee = map(int, self.__date_naissance.split("/"))
		date_naissance = date(annee, mois, jour)
		date_ajd = date.today()
		age = aujourd_hui.year - date_naissance.year
		if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
			age -= 1
			return age
	




	#endregion





	def nourrir(self, animal):
		"""
		Nourrit seulement si on est le soigneur de l'animal
		"""
		if not hasattr(self, 'nom') or not hasattr(animal, 'soigneur'):
			return "[Erreur] Soigneur ou animal non défini"

		if self != animal.soigneur:
			return f"{self.nom} n'est pas le soigneur de {animal.nom}"

		animal.appetit = max(0, animal.appetit - 40)
		animal.satisfaction = min(100, animal.satisfaction + 10)
		return (f" {self.nom} a nourri {animal.nom} !\n"
				f" Appétit maintenant : {animal.appetit}/100")

	def entretenir(self, animal):
		"""
		Entretient seulement si responsable
		"""
		if not hasattr(self, 'nom') or not hasattr(animal, 'soigneur'):
			return "[Erreur] Soigneur ou animal non défini"

		if self != animal.soigneur:
			return f"{self.nom} n'est pas le soigneur de {animal.nom}"

		animal.satisfaction = min(100, animal.satisfaction + 35)

		return (f" {self.nom} a entretenu {animal.nom} !\n"
				f" Satisfaction maintenant : {animal.satisfaction}/100")

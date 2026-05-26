from datetime import datetime

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
	def age(self):
		if not hasattr (self, '__date_naissance'):
			return 0
		try:
			date_naissance = datetime.strptime(self.__date_naissance, "%d/%m/%Y")
			date_du_jour = datetime.today()
			anniversaire_passe = ((date_du_jour.month, date_du_jour.day) < (date_naissance.month, date_naissance.day)) # est égal à 1 ou 0 -- s'il n'est pas encore passé, on enlève un an en plus
			age = date_du_jour.year - date_naissance.year - anniversaire_passe
			return age
		except ValueError:
			return "Date de naissance invalide (format attendu : JJ/MM/AAAA)"
	

	#endregion

	def nourrir(self, animal):
		"""
		Nourrit seulement si on est le soigneur de l'animal
		"""
		if not hasattr(self, 'nom') or not hasattr(animal, 'soigneur'):
			return "[Erreur] Soigneur ou animal non défini"

		if self != animal.soigneur:
			return f"{self.nom} n'est pas le soigneur de {animal.nom}"

		animal.manger()
		#animal.satisfaction = min(100, animal.satisfaction + 10) pas besoin de gérer cette ligne puisque l'animal gagne de la satisfaction avec l'action manger
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
	

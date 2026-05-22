from datetime import datetime


class Soigneur:

	#region Attributs

	def definir(self, nom, date_naissance, experience, nombre_animaux_responsable=0):
		self.__nom = nom
		self.__date_naissance = date_naissance
		self.__experience = experience
		self.__nombre_animaux_responsable = nombre_animaux_responsable
		return f"Soigneur {nom} créé"


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
		if not hasattr(self, 'date_naissance'):
			print("if")
			return 0
		try:
			print('try')
			date_naissance_recup = datetime.strptime(self.__date_naissance, "%d/%m/%Y")
			date_du_jour = datetime.today()
			anniversaire_est_passe = (date_du_jour.month, date_du_jour.day) < (date_naissance_recup.month, date_naissance_recup.day)
			age = date_du_jour.year - date_naissance_recup.year - anniversaire_est_passe

			return age
		except ValueError:
			return "Date de naissance invalide (format attendu : JJ/MM/AAAA)"

	#endregion

	#region Methodes

	def nourrir(self, animal):
		"""
		Nourrit seulement si on est le soigneur de l'animal
		"""
		if not hasattr(self, 'nom') or not hasattr(animal, 'soigneur'):
			return "[Erreur] Soigneur ou animal non défini"

		if self != animal.soigneur:
			return f"{self.nom} n'est pas le soigneur de {animal.nom}"

		animal.manger()
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

		animal.laver(self)

		return (f" {self.nom} a entretenu {animal.nom} !\n"
				f" Satisfaction maintenant : {animal.satisfaction}/100")

	#endregion


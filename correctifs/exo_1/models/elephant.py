class Elephant:

	def definir(self, nom, appetit=50, satisfaction=50, en_vie=True, soigneur=None):
		self.nom = nom
		self.appetit = max(0, min(100, appetit))
		self.satisfaction = max(0, min(100, satisfaction))
		self.en_vie = en_vie
		self.soigneur = soigneur
		return f"Éléphant {nom} créé"

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
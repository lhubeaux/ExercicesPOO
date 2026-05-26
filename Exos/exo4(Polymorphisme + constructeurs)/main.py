from models import Soigneur, Elephant, Enclos, Giraffe, Animal

def main():
	print("=" * 15)
	print("Correctif Exo_2")
	print("=" * 15 + "\n")

	# Création du soigneur
	soigneur = Soigneur()
	
	print(soigneur.definir("Dr House","14/3/1975", 12))

	# Création des éléphants + lien avec les soigneur 
	babar = Elephant("Babar", appetit=40, satisfaction=80, soigneur=soigneur)

	dumbo = Elephant("Dumbo", appetit=70, satisfaction=50, soigneur=soigneur)

	# Création giraffes

	giraffe_1 = Giraffe("Manny", appetit=50, satisfaction=50, soigneur=soigneur)

	# Création de l'enclos + ajout des animaux
	savane = Enclos()
	print(savane.definir("Savane", 5, "Grand"))
	print(savane.ajouter_animal(dumbo))
	print(savane.ajouter_animal(babar))
	print(savane.ajouter_animal(giraffe_1))

	# Affichage
	print(savane.aficher_animaux())

	# actions soigneur
	print(soigneur.nourrir(dumbo))
	print()
	print(soigneur.entretenir(babar))
	print()

	print(f"Age soigneur : {soigneur.age}")
# L'éléphant mange tout seul
	print(dumbo.manger())
	print()

	print(giraffe_1.manger_feuilles())
	print(babar.observer_environnements())
	print(dumbo.aspirer_eau())
# # Bonus...
# 	print(savane.passer_jour())
# 	print(savane.passer_jour())
# 	print(savane.passer_jour())
# 	print(savane.passer_jour())

	def declencher_bruit(animal):
		print(animal.faire_bruit())

	declencher_bruit(giraffe_1)

	# Affichage Final 👿

if __name__ == "__main__":
	main()

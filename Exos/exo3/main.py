from models import Soigneur, Elephant, Enclos, Giraffe

def main():
	print("=" * 15)
	print("Correctif Exo_2")
	print("=" * 15 + "\n")

	# Création du soigneur
	soigneur = Soigneur()
	
	print(soigneur.definir("Dr House","14/3/1975", 12))

	# Création des éléphants + lien avec les soigneur 
	babar = Elephant()
	print(babar.definir("Babar", appetit=40, satisfaction=80, soigneur=soigneur))

	dumbo = Elephant()
	print(dumbo.definir("Dumbo", appetit=70, satisfaction=50, soigneur=soigneur))

	# Création giraffes

	giraffe_1 = Giraffe()
	print(giraffe_1.definir("Manny", appetit=50, satisfaction=50, soigneur=soigneur))

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
# Bonus...
	print(savane.passer_jour())
	print(savane.passer_jour())
	print(savane.passer_jour())
	print(savane.passer_jour())

	print(babar.longueur_defense)
	print(giraffe_1.manger_feuilles())
	print(babar.bain_de_boue())
	print(dumbo.aspirer_eau())

	# Affichage Final 👿

if __name__ == "__main__":
	main()
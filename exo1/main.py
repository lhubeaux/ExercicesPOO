from models import Elephant, Soigneur, Enclos

import random

eleph_1 = Elephant()
eleph_2 = Elephant()
eleph_1.definir_elephant("Jean-Michel", 100, 100, "personne")
eleph_2.definir_elephant("Albertine", 100, 100, "personne")

print("Un nouveau joueur commence: les éléphants ont faim et ils s'embêtent...")

eleph_1.appetit = random.randint(1, 100)
eleph_2.appetit = random.randint(1, 100)
eleph_1.satisfaction = random.randint(1, 100)
eleph_2.satisfaction = random.randint(1, 100)


soigneur_1 = Soigneur()
soigneur_1.definir_soigneur("Fred", "25-10-1990", 10)

enclos_1 = Enclos()
enclos_1.definir_enclos("Enclos 1", 10, 10)

def main():

    print(eleph_1.afficher_elephant())
    print(eleph_2.afficher_elephant())


    print(soigneur_1.ajouter_animal(eleph_1))
    print(soigneur_1.nourrir(eleph_1))
    print(soigneur_1.entretenir(eleph_1))

    print(soigneur_1.ajouter_animal(eleph_2))
    print(soigneur_1.nourrir(eleph_2))
    print(soigneur_1.entretenir(eleph_2))

    enclos_1.ajouter_animal(eleph_1)
    enclos_1.ajouter_animal(eleph_2)
    print(enclos_1.afficher_animaux())


if __name__ == "__main__":
    main()
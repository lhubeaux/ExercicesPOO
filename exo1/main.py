from models import Elephant, Soigneur, Enclos

eleph_1 = Elephant()
eleph_2 = Elephant()
eleph_1.definir_elephant("Jean-Michel", 85, 90, "personne")
eleph_2.definir_elephant("Albertine", 50, 90, "personne")


def main():

    print(eleph_1.afficher_elephant())
    print(eleph_2.afficher_elephant())

    soigneur_1 = Soigneur()
    soigneur_1.definir_soigneur("Fred", "25-10-1990", 10)

    print(soigneur_1.ajouter_animal(eleph_1))
    print(soigneur_1.nourrir(eleph_1))
    print(soigneur_1.entretenir(eleph_1))

    print(soigneur_1.ajouter_animal(eleph_2))
    print(soigneur_1.nourrir(eleph_2))
    print(soigneur_1.entretenir(eleph_2))


    enclos_1 = Enclos()
    enclos_1.definir_enclos("Enclos 1", 10, 10)
    enclos_1.ajouter_animal(eleph_1)
    enclos_1.ajouter_animal(eleph_2)
    print(enclos_1.afficher_animaux())


if __name__ == "__main__":
    main()
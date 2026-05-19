from models import Elephant, Soigneur

eleph_1 = Elephant()
eleph_1.definir_elephant("Jean-Michel", 85, 90, "Fred")

print(eleph_1.afficher_elephant())

soigneur_1 = Soigneur()
soigneur_1.definir_soigneur("Fred", "25-10-1990", 10)

print(soigneur_1.ajouter_animal(eleph_1))
print(soigneur_1.nourrir(eleph_1))
print(soigneur_1.entretenir(eleph_1))

print(eleph_1.afficher_elephant())






if __name__ == "__main__":
    main()
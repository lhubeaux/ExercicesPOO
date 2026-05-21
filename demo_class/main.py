from models import Voiture, Garage #grâce au __init__.py on peut appeler tous les objets sur une seule ligne

def main():
    voiture_1 = Voiture()
    voiture_2 = Voiture()
    
    voiture_1.definir_voiture("Porsche", "Carrera", "Rouge", "2006", 86452)
    voiture_2.definir_voiture("Porsche", "911.992", "Jaune", "2012", 86442)

    garage = Garage()
    garage.ajouter_voiture(voiture_1)
    garage.ajouter_voiture(voiture_2)

    print(garage.afficher_toutes_voitures())

    # print(voiture_1.demarrer())
    # print(voiture_2.demarrer())

    print("Getter")
    print(f"Couleur :  {voiture_1.couleur}")  #Appelle  le getter

    print("Setter")
      #test des erreurs
    try:
        voiture_1.couleur = 123
    except TypeError as e:
        print(f"[Erreur] {e}")
    print(f"Nouvelle couleur : {voiture_1.couleur}")




if __name__ == "__main__":
    main()



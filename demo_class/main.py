from models import Voiture, Garage, VoitureElectrique #grâce au __init__.py on peut appeler tous les objets sur une seule ligne

def main():
    voiture = Voiture()
    voiture_elec = VoitureElectrique()
    
    voiture.definir("Porsche", "Carrera", "Rouge", 2006, 86452)
    voiture_elec.definir("Porsche", "911.Taycan", 2019, "Jaune", 86442, 350)

    garage = Garage()
    garage.ajouter_voiture(voiture)
    garage.ajouter_voiture(voiture_elec)

    # print(garage.afficher_toutes_voitures())

    print(voiture.demarrer())
    print(voiture_elec.demarrer())

    print(voiture_elec.afficher_info())

    # print("Getter")
    # print(f"Couleur :  {voiture_1.couleur}")  #Appelle  le getter

    # print("Setter")
    #   #test des erreurs
    # try:
    #     voiture_1.couleur = 123
    # except TypeError as e:
    #     print(f"[Erreur] {e}")
    # print(f"Nouvelle couleur : {voiture.couleur}")




if __name__ == "__main__":
    main()



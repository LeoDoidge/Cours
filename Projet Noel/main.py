# main.py

# Partie 1 : Structure de données
cadeaux = [
    {"nom": "Ours en peluche", "poids": 2, "maison": "Maison A"},
    {"nom": "Voiture jouet", "poids": 1, "maison": "Maison B"},
    {"nom": "Poupée", "poids": 3, "maison": "Maison A"},
    {"nom": "Puzzle", "poids": 4, "maison": "Maison C"},
    {"nom": "Jeu de société", "poids": 5, "maison": "Maison B"},
]


def afficher_cadeaux(cadeaux):
    for cadeau in cadeaux:
        print(
            f"Cadeau : {cadeau['nom']}, Poids : {cadeau['poids']}kg, Maison : {cadeau['maison']}"
        )


# Partie 2 : Tri des cadeaux
def trier_cadeaux_par_poids(cadeaux, decroissant=False):
    return sorted(cadeaux, key=lambda x: x["poids"], reverse=decroissant)


def filtrer_cadeaux_par_maison(cadeaux, maison):
    return [cadeau for cadeau in cadeaux if cadeau["maison"] == maison]


# Partie 3 : Optimisation avec un algorithme glouton
def optimiser_cadeaux_pour_traineau(cadeaux, poids_max=20):
    cadeaux_tries = trier_cadeaux_par_poids(cadeaux)
    cadeaux_selectionnes = []
    poids_total = 0

    for cadeau in cadeaux_tries:
        if poids_total + cadeau["poids"] <= poids_max:
            cadeaux_selectionnes.append(cadeau)
            poids_total += cadeau["poids"]
        else:
            break

    return cadeaux_selectionnes, poids_total


# Exemple d'utilisation
if __name__ == "__main__":
    print("Tous les cadeaux :")
    afficher_cadeaux(cadeaux)

    print("\nCadeaux triés par poids (croissant) :")
    cadeaux_tries = trier_cadeaux_par_poids(cadeaux)
    afficher_cadeaux(cadeaux_tries)

    print("\nCadeaux pour la maison 'Maison A' :")
    maison_a_cadeaux = filtrer_cadeaux_par_maison(cadeaux, "Maison A")
    afficher_cadeaux(maison_a_cadeaux)

    print("\nOptimisation des cadeaux pour le traîneau :")
    cadeaux_selectionnes, poids_total = optimiser_cadeaux_pour_traineau(cadeaux)
    afficher_cadeaux(cadeaux_selectionnes)
    print(f"Poids total des cadeaux sélectionnés : {poids_total}kg")

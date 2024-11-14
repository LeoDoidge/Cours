class Livre:
    def __init__(self):
        # Constructeur de la classe Livre pour initialiser les attributs
        self.titre = str(input("Entrez le titre du livre: "))
        self.auteur = str(input("Entrez l'auteur: "))
        self.publication = int(input("Entrez l'année de publication: "))
        self.genre = str(input("Entrez le genre: "))

def ChoicePrint():
    # Affiche le menu des options disponibles pour l'utilisateur
    print("\nMenu:")
    print("1: Ajouter un nouveau livre")
    print("2: Afficher la liste des livres")
    print("3: Rechercher un livre")
    print("4: Modifier un livre")
    print("5: Supprimer un livre")
    print("6: Quitter le programme")
    print()

# Initialisation de la bibliothèque et des variables globales
library = {}  # Dictionnaire pour stocker les livres avec leur ID
RUNNING = True  # Variable pour contrôler la boucle principale
POINTER = 0  # Indicateur pour la gestion de l'entrée utilisateur
BOOK_POINTER = 1  # ID unique pour chaque livre

while RUNNING:
    ChoicePrint()  # Affiche le menu

    if POINTER == 0:
        # Demande à l'utilisateur de faire un choix dans le menu
        choice = int(input("Entrez votre choix: "))
        POINTER += 1

    if choice == 1:  # Ajout d'un nouveau livre
        newbook = Livre()  # Crée une nouvelle instance de Livre
        library[BOOK_POINTER] = newbook  # Ajoute le livre dans la bibliothèque
        BOOK_POINTER += 1  # Incrémente l'ID pour le prochain livre

    if choice == 2:  # Affichage de la liste de livres
        if library:
            print("Liste de livres dans la bibliothèque:")
            for book_id, livre in library.items():
                print(f"ID {book_id}: {livre.titre}")
        else:
            print("Il n'y a pas de livre dans la bibliothèque")

    if choice == 3:  # Recherche d'un livre
        search_id = int(input("Quel livre cherchez-vous (ID): "))
        if search_id in library:
            # Affiche les informations du livre trouvé
            livre = library[search_id]
            print(f"Livre trouvé: {livre.titre}, Auteur: {livre.auteur}, "
                  f"Année: {livre.publication}, Genre: {livre.genre}")
        else:
            print(f"Le livre avec l'ID {search_id} n'existe pas.")

    if choice == 4:  # Modification d'un livre
        book_id = int(input("Entrez l'ID du livre à modifier: "))
        if book_id in library:
            livre = library[book_id]
            print(f"Informations actuelles du livre : {livre.titre}, Auteur: {livre.auteur}, "
                  f"Année: {livre.publication}, Genre: {livre.genre}")

            # Menu pour choisir l'information à modifier
            print("Que voulez-vous modifier ?")
            print("1: Titre")
            print("2: Auteur")
            print("3: Année de publication")
            print("4: Genre")
            choice_modification = int(input("Entrez votre choix: "))

            # Modification selon le choix de l'utilisateur
            if choice_modification == 1:
                livre.titre = input("Entrez le nouveau titre: ")
            elif choice_modification == 2:
                livre.auteur = input("Entrez le nouvel auteur: ")
            elif choice_modification == 3:
                livre.publication = int(input("Entrez la nouvelle année de publication: "))
            elif choice_modification == 4:
                livre.genre = input("Entrez le nouveau genre: ")
            else:
                print("Choix invalide.")
            print("Livre modifié avec succès!")
        else:
            print(f"Le livre avec l'ID {book_id} n'existe pas.")

    if choice == 5:  # Suppression d'un livre
        search_id = int(input("Entrez l'ID du livre à supprimer: "))
        if search_id in library:
            del library[search_id]
            print("Le livre a été supprimé.")
        else:
            print("Le livre n'est pas dans la bibliothèque.")

    if choice == 6:  # Quitter le programme
        RUNNING = False
        print("Programme terminé.")

    POINTER = 0  # Réinitialise le pointeur pour permettre un nouveau choix

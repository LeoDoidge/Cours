class Livre:
    def __init__(self):
        self.titre = str(input("Entrez le titre du livre: "))
        self.auteur = str(input("Entrez l'auteur: "))
        self.publication = int(input("Entez l'annee de publication: "))
        self.genre = str(input("Entrez le genre: "))

    def ListeLivre(self):
        pass

    def RechercherLivre(self):
        pass

    def ModifierLivre(self):
        pass

    def SupprimerLivre(self):
        pass

    def DisplayInfo(self):
        return print(
            f"Titre: {self.titre}, Auteur:{self.auteur},"
            f"Annee de publication: {self.publication}, Genre: {self.genre}"
        )


def ChoicePrint():
    print("\nMenu:")
    print("1: Ajouter un nouveau livre")
    print("2: Afficher la liste des livres")
    print("3: Rechercher un livre")
    print("4: Modifier un livre")
    print("5: Supprimer un livre")
    print("6: Quitter le programme")
    print()


library = {}
RUNNING = True
POINTER = 0
BOOK_POINTER = 1
while RUNNING:

    ChoicePrint()

    if POINTER == 0:
        choice = int(input("Entrez votre choix"))
        POINTER += 1

    if choice == 1: # Ajout d'un nouveau livre
        newbook = Livre()
        library[BOOK_POINTER] = newbook
        BOOK_POINTER += 1

    if choice == 2: # Affichage de la liste de livre
        if library:
            print("Liste de livre dans la librairie: ")
            for book_id, livre in library.items():
                print(f"ID {book_id}: {livre.titre}")
        else:
            print("Il n'y a pas de livre dans la bibliotheque")

    if choice == 3: # Recherche du livre
        search_id = int(input("Quelle livre cherchez vous: "))
        if search_id in library:
            print(f'Livre trouver: {library[search_id].DisplayInfo()}')
        else:
            print(f'Livre {search_id} does not exist')

    if choice == 4: # Modifier un livre
        pass

    if choice == 5: # Supprimer un livre
        pass

    if choice == 6: # Quitter le programme
        RUNNING = False

    POINTER = 0

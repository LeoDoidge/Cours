class Livre:
    def __init__(self, titre=None, auteur=None, publication=None, genre=None):
        """Initialisation avec des paramètres par défaut pour faciliter les tests."""
        self.titre = titre if titre else str(input("Entrez le titre du livre: "))
        self.auteur = auteur if auteur else str(input("Entrez l'auteur: "))
        self.publication = (
            publication
            if publication
            else int(input("Entrez l'année de publication: "))
        )
        self.genre = genre if genre else str(input("Entrez le genre: "))


def AjouterLivre(library, book_pointer, livre):
    """Ajoute un livre à la bibliothèque."""
    library[book_pointer] = livre
    return book_pointer + 1  # Incrémente et retourne le nouveau book_pointer


def AfficherLivres(library):
    """Affiche tous les livres de la bibliothèque."""
    if library:
        for book_id, livre in library.items():
            print(
                f"ID {book_id}: {livre.titre}, Auteur: {livre.auteur}, "
                f"Année: {livre.publication}, Genre: {livre.genre}"
            )
    else:
        print("Il n'y a pas de livre dans la bibliothèque.")


def RechercherLivre(library, search_id):
    """Recherche un livre par ID."""
    return library.get(search_id, None)


def ModifierLivre(library, book_id):
    """Modifie un livre existant."""
    if book_id in library:
        livre = library[book_id]
        print(
            f"Informations actuelles du livre : {livre.titre}, Auteur: {livre.auteur}, "
            f"Année: {livre.publication}, Genre: {livre.genre}"
        )

        # Menu pour choisir l'information à modifier
        print("Que voulez-vous modifier ?")
        print("1: Titre")
        print("2: Auteur")
        print("3: Année de publication")
        print("4: Genre")
        try:
            choice_modification = int(input("Entrez votre choix: "))
        except ValueError:
            print("Choix invalide.")
            return

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


def SupprimerLivre(library, book_id):
    """Supprime un livre par ID."""
    if book_id in library:
        del library[book_id]
        print("Le livre a été supprimé.")
        return True
    else:
        print("Le livre n'est pas dans la bibliothèque.")
        return False


# Boucle principale du programme
def Main():
    library = {}
    book_pointer = 1
    running = True

    while running:
        print("\nMenu:")
        print("1: Ajouter un nouveau livre")
        print("2: Afficher la liste des livres")
        print("3: Rechercher un livre")
        print("4: Modifier un livre")
        print("5: Supprimer un livre")
        print("6: Quitter le programme")
        print()

        try:
            choice = int(input("Entrez votre choix: "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if choice == 1:  # Ajouter un livre
            newbook = Livre()
            book_pointer = AjouterLivre(library, book_pointer, newbook)

        elif choice == 2:  # Afficher la liste des livres
            AfficherLivres(library)

        elif choice == 3:  # Rechercher un livre
            try:
                search_id = int(input("Entrez l'ID du livre que vous cherchez: "))
                livre = RechercherLivre(library, search_id)
                if livre:
                    print(
                        f"Livre trouvé: {livre.titre}, Auteur: {livre.auteur}, "
                        f"Année: {livre.publication}, Genre: {livre.genre}"
                    )
                else:
                    print(f"Aucun livre avec l'ID {search_id}.")
            except ValueError:
                print("Veuillez entrer un ID valide.")

        elif choice == 4:  # Modifier un livre
            try:
                book_id = int(input("Entrez l'ID du livre à modifier: "))
                ModifierLivre(library, book_id)
            except ValueError:
                print("Veuillez entrer un ID valide.")

        elif choice == 5:  # Supprimer un livre
            try:
                book_id = int(input("Entrez l'ID du livre à supprimer: "))
                SupprimerLivre(library, book_id)
            except ValueError:
                print("Veuillez entrer un ID valide.")

        elif choice == 6:  # Quitter le programme
            running = False
            print("Programme terminé.")
        else:
            print("Veuillez entrer un nombre entre 1 et 6.")


if __name__ == "__main__":
    Main()

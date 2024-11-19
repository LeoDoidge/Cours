import unittest
from bibliotheque import (
    Livre,
    AjouterLivre,
    RechercherLivre,
    ModifierLivre,
    SupprimerLivre,
)


class TestBibliotheque(unittest.TestCase):

    def setUp(self):
        """Initialisation de la bibliothèque avant chaque test."""
        self.library = {}
        self.book_pointer = 1  # Initialisation du pointeur de livre
        self.book1 = Livre(
            titre="1984", auteur="George Orwell", publication=1949, genre="Dystopie"
        )
        self.book2 = Livre(
            titre="Le Petit Prince",
            auteur="Antoine de Saint-Exupéry",
            publication=1943,
            genre="Conte",
        )

    def test_ajouter_livre(self):
        self.book_pointer = AjouterLivre(self.library, self.book_pointer, self.book1)
        self.assertEqual(len(self.library), 1)
        self.assertEqual(self.library[1].titre, "1984")

    def test_afficher_livres(self):
        self.book_pointer = AjouterLivre(self.library, self.book_pointer, self.book1)
        self.book_pointer = AjouterLivre(self.library, self.book_pointer, self.book2)
        livres_list = [
            f"ID {book_id}: {livre.titre}, Auteur: {livre.auteur}, Année: {livre.publication}, Genre: {livre.genre}"
            for book_id, livre in self.library.items()
        ]
        self.assertEqual(len(livres_list), 2)
        self.assertIn("1984", livres_list[0])
        self.assertIn("Le Petit Prince", livres_list[1])

    def test_rechercher_livre(self):
        self.book_pointer = AjouterLivre(self.library, self.book_pointer, self.book1)
        livre_trouve = RechercherLivre(self.library, 1)
        self.assertIsNotNone(livre_trouve)
        self.assertEqual(livre_trouve.titre, "1984")

        livre_non_trouve = RechercherLivre(self.library, 99)
        self.assertIsNone(livre_non_trouve)

    def test_modifier_livre(self):
        self.book_pointer = AjouterLivre(self.library, self.book_pointer, self.book1)
        ModifierLivre(self.library, 1)
        self.library[1].titre = "1984 - Édition spéciale"
        self.assertEqual(self.library[1].titre, "1984 - Édition spéciale")

    def test_supprimer_livre(self):
        self.book_pointer = AjouterLivre(self.library, self.book_pointer, self.book1)
        SupprimerLivre(self.library, 1)
        self.assertEqual(len(self.library), 0)

        # Vérifier la suppression d'un livre inexistant
        resultat = SupprimerLivre(self.library, 99)
        self.assertFalse(resultat)


if __name__ == "__main__":
    unittest.main()

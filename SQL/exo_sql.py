import sqlite3
import os


def Exo1():

    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Full path to the database file in the same location as the script
    db_path = os.path.join(script_directory, "mynewbase.db")

    # Connect to the database
    connexion = sqlite3.connect(db_path)

    # Récupération d'un curseur
    c = connexion.cursor()

    # ---- début des instructions SQL

    # Création de la table
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS bulletin(
        Name TEXT,
        Grade INT);
        """
    )

    lst_notes = []
    running = True
    while running:
        name = str(input("Nom? "))
        if name == "q" or name == "Q":
            print("ending boucle")
            break
        grade = int(input("Note? "))
        data = (name, grade)
        lst_notes.append(data)

    c.executemany("""INSERT INTO bulletin VALUES (?, ?)""", lst_notes)
    # ---- fin des instructions SQL

    # Validation
    connexion.commit()

    # Déconnexion
    connexion.close()


""""--------------------------------------------------------------------------------"""


#Connexion
connexion = sqlite3.connect('mabasecobaye.db')

#Récupération d'un curseur
c = connexion.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS notes(
    Nom TEXT,
    Note INT);
    """)


while True :
    nom = input('Nom ? ')
    if nom in ['Q','q'] :
        break
    note = input('Note ? ')
    data = (nom, note)
    p = "INSERT INTO notes VALUES ('" + nom + "','" + note + "')"

    c.executescript(p)


#Validation
    connexion.commit()


#Déconnexion
connexion.close()

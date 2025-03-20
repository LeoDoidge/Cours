def Exo1():
    a = {
        "F": ["B", "G"],
        "B": ["A", "G"],
        "A": ["", ""],
        "D": ["C", "E"],
        "C": ["", ""],
        "E": ["", ""],
        "G": ["", "I"],
        "I": ["", "H"],
        "H": ["", ""],
    }

    def Taille(arbre, lettre):
        if lettre == "":
            return 0
        return 1 + Taille(arbre, arbre[lettre][0]) + Taille(arbre, arbre[lettre][1])

    print(Taille(a, "F"))


def Exo2():
    tab = [41, 55, 21, 18, 12, 6, 25]

    def Echange(tab, i, j):
        temp = tab[i]
        tab[i] = tab[j]
        tab[j] = temp

    def TriSelection(tab):
        n = len(tab)
        for k in range(n):
            imin = k
            for i in range(k + 1, n):
                if tab[i] < tab[imin]:
                    imin = i
            Echange(tab, k, imin)

    TriSelection(tab)
    print(tab)


def Exo3():
    table_1 = [0, 1, 1, 1, 0]
    table_2 = [1, 0, 1, 0, 1]

    def ou_exclusif(t_1, t_2):
        resultat = []
        for i in range(len(t_1)):
            if t_1[i] == t_2[i]:
                resultat.append(0)
            else:
                resultat.append(1)
        return resultat

    print(ou_exclusif(table_1, table_2))


def Exo4():
    class Carre:
        def __init__(self, liste, n):
            self.ordre = n
            self.tableau = [[liste[i + j * n] for i in range(n)] for j in range(n)]

        def affiche(self):
            for i in range(self.ordre):
                print(self.tableau[i])

        def somme_ligne(self, i):
            somme = 0
            for j in range(self.ordre):
                somme += self.tableau[i][j]
            return somme

        def somme_col(self, j):
            somme = 0
            for i in range(self.ordre):
                somme += self.tableau[i][j]
            return somme

        def est_semimagique(self):
            s = self.somme_ligne(0)
            for i in range(1, self.ordre):
                if self.somme_ligne(i) != s:
                    return False
            for j in range(self.ordre):
                if self.somme_col(j) != s:
                    return False
            return True

    c = Carre([2, 7, 6, 9, 5, 1, 4, 3, 8], 3)
    c.affiche()
    print(c.est_semimagique())


def Exo5():
    def correspond(mot, mot_a_trous):
        if len(mot) != len(mot_a_trous):
            return False
        for i in range(len(mot)):
            if mot_a_trous[i] != "*" and mot_a_trous[i] != mot[i]:
                return False
        return True

    print(correspond("informatique", "info*ma*ique"))
    print(correspond("stop", "s*"))
    print(correspond("auto", "*ut*"))


def Exo6():
    def est_cyclique(plan : dict) -> bool:
        expediteur = "a"
        destinataire = plan[expediteur]
        nb_destinataires = 1
        
        while destinataire != expediteur:
            destinataire = plan[destinataire]
            nb_destinataires += 1
        
        return nb_destinataires == len(plan)

    print(est_cyclique({"a": "e", "f": "a", "c": "d", "e": "b", "b": "f", "d": "c"}))
    print(est_cyclique({"a": "e", "f": "c", "c": "d", "e": "b", "b": "f", "d": "a"}))
    print(est_cyclique({"a": "b", "f": "c", "c": "d", "e": "a", "b": "f", "d": "e"}))
    print(est_cyclique({"a": "b", "f": "a", "c": "d", "e": "c", "b": "f", "d": "e"}))


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
    tab = [ 41, 55, 21, 18, 12, 6, 25]

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

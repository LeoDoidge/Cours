def Day1():
    def Inverse(liste):
        final_list = []
        for i in range(len(liste)):
            final_list.append(liste[len(liste) - i - 1])
        return final_list

    def Double(liste):
        final_list = []
        for i in range(len(liste)):
            if liste[i] not in final_list:
                final_list.append(liste[i])
        return final_list

    class Pile:
        def __init__(self):
            self.liste = []

        def Empiler(self, element):
            self.liste.append(element)

        def Depiler(self):
            if len(self.liste) == 0:
                return None
            return self.liste.pop()

        def EstVide(self):
            return len(self.liste) == 0

    class File:
        def __init__(self):
            self.pile1 = Pile()
            self.pile2 = Pile()

        def Enfiler(self, element):
            self.pile1.empiler(element)

        def Defiler(self):
            if self.pile2.est_vide():
                while not self.pile1.est_vide():
                    self.pile2.empiler(self.pile1.depiler())
            return self.pile2.depiler()

        def EstVide(self):
            return self.pile1.est_vide() and self.pile2.est_vide()


def Day2():

    graphe_liste_adjacence = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    sommets = ["A", "B", "C", "D"]

    taille = len(sommets)
    graphe_matrice_adjacence = [[0] * taille for _ in range(taille)]
    index_sommets = {sommets[i]: i for i in range(taille)}
    aretes = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
    for debut, fin in aretes:
        i = index_sommets[debut]
        j = index_sommets[fin]
        graphe_matrice_adjacence[i][j] = 1
    print("Liste d'adjacence:", graphe_liste_adjacence)
    print("Matrice d'adjacence:")
    for ligne in graphe_matrice_adjacence:
        print(ligne)

    def BFS(graphe, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(
                    [neighbor for neighbor in graphe[vertex] if neighbor not in visited]
                )

        return result

    def DFS(graphe, start):
        visited = set()
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                stack.extend(
                    [neighbor for neighbor in graphe[vertex] if neighbor not in visited]
                )

        return result

    print("BFS:", BFS(graphe_liste_adjacence, "A"))
    print("DFS:", DFS(graphe_liste_adjacence, "A"))

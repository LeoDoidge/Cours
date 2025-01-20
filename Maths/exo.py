a = []
b = []
c = []
matrice = [
    a,
    b,
    c,
]


def Exchange(x, y, matrix=list):

    new_matrix = [[], [], []]
    new_matrix = matrix
    new_matrix[y] = matrix[x]
    new_matrix[x] = matrix[y]

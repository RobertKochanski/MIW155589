import numpy as np


def getcofactor(m, i, j):
    return [row[: j] + row[j + 1:] for row in (m[: i] + m[i + 1:])]


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0]

    if len(matrix) == 2:
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return value

    sum = 0

    for current_column in range(len(matrix)):
        sign = (-1) ** current_column
        sub_det = determinant(getcofactor(matrix, 0, current_column))
        sum += (sign * matrix[0][current_column] * sub_det)

    return sum


A = [2]
B = [
    [1, 2, 4],
    [3, 4, 7],
    [5, 6, 7],
]
C = [
    [1, 2, 3, 4],
    [4, 3, 5, 6],
    [8, 4, 2, 1],
    [3, 2, 4, 1],
]
D = [
    [1, 3, 5, 7, 9],
    [4, 6, 3, 7, 5],
    [1, 5, 3, 7, 6],
    [5, 10, 8, 3, 1],
    [8, 1, 7, 5, 8],
]
print("Wyznacznik A --> ", determinant(A))
print("Wyznacznik B --> ", determinant(B))
print("Wyznacznik C --> ", determinant(C))
print("Wyznacznik D --> ", determinant(D))


def wyznacznik_spr(matrix):
    wyz = np.linalg.det(matrix)
    wynik = round(wyz, 0)
    print(wynik)


# wyznacznik_spr(A) NIE MOŻNA SPRAWDZIĆ, musi być macierz conajmniej 2 wymiarowa, ale chyba wyznacznik jest oczywisty.
wyznacznik_spr(B)
wyznacznik_spr(C)
wyznacznik_spr(D)

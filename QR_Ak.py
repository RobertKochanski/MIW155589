import copy
import math

import numpy as np
from numpy.linalg import inv


# macierz QR
def iloczynSkalarny(wektorA, wektorB):
    return np.dot(np.array(wektorA.T), np.array(wektorB))


def projekcja(v, u):
    return iloczynSkalarny(v, u) / iloczynSkalarny(u, u) * u  # przykład: ((v2 * u1) / (u1 * u1)) * u1)


def oblicz_e(wektor):
    return np.dot(wektor, 1 / math.sqrt(iloczynSkalarny(wektor, wektor)))  # przykład: u2 * (1 / sqrt(u2 * u2))


def QR(macierz):
    Q = []
    U = []
    petla = 1

    print(f'--------------- MACIERZ POCZĄTKOWA A --------------- \n'
          f'A:\n{macierz}')

    for i in range(len(macierz[0])):
        sumaP = 0
        wektor_v = np.array(macierz[:, i]).reshape((len(macierz), 1))
        for j in range(i):
            sumaP += projekcja(wektor_v, U[j])
        wektor_u = wektor_v - sumaP
        U.append(wektor_u)
        wektor_e = oblicz_e(wektor_u)
        Q.append(wektor_e[:, 0])
        print(f'--------------- OBLICZENIA DLA e{petla} --------------- \n'
              f'v{petla}:\n{wektor_v} \n'
              f'u{petla}:\n{wektor_u} \n'
              f'e{petla}:\n{wektor_e} \n')
        petla += 1

    print(f'--------------- WYNIK ---------------')
    R = np.dot(np.array(Q), macierz)
    QR = np.dot(np.array(Q).T, R)
    print(f'Q:\n{np.round(np.array(Q).T, 3)} \n'
          f'R:\n{np.round(np.array(R), 3)} \n'
          f'QR:\n{np.round(np.array(QR), 3) + 0}')  # '+ 0' usuwa minus przy wyniku np. '-0'

    return Q, R


A = np.array([
    [2, 0],
    [0, 1],
    [1, 2]
])

QR(A)


# Wartości własne macierzy
# print("\n\nLambda: ", np.linalg.eigvals(A))

# Q^-1 * A * Q
def a_k(A, k):
    if A.shape[0] != A.shape[1]:
        raise 'Macierze nie jest kwadratowa.'
    matrix = copy.deepcopy(A)
    for i in range(k):
        Q, R = QR(matrix)
        matrix = np.linalg.inv(Q) @ matrix @ Q
    return np.round(matrix, 3)


# print("\n\n", a_k(A, 100))

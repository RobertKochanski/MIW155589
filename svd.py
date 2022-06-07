import math
import numpy as np
from numpy.linalg import eigh, norm


#  A  =  U  *  S  *  VT
# mxn = mxm * mxn * nxn

def svd(A):
    m, n = A.shape

    AAT = A @ A.T
    ATA = A.T @ A

    sigma = np.zeros(A.shape)
    U_wartosci_w, U = np.linalg.eigh(AAT)
    V_wartosci_w, V = np.linalg.eigh(ATA)

    if AAT.shape[0] >= ATA.shape[0]:

        U_wartosci_w = sorted(U_wartosci_w, reverse=True)

        for x in range(n):
            sigma[x][x] = math.sqrt(U_wartosci_w[x])
        print("### SIGMA ### \n", sigma, "\n")

        for i in range(n):
            U[i] = A @ V[:, i]/norm(A @ V[:, i])

        print(U, "\n")
        print(V.T, "\n")
        print(U @ sigma @ V.T, "\n")

    else:
        V_wartosci_w = sorted(V_wartosci_w, reverse=True)

        for x in range(m):
            sigma[x][x] = math.sqrt(V_wartosci_w[x])
        print("### SIGMA ### \n", sigma, "\n")

        for i in range(m):
            V[i] = A.T @ U[i]/norm(A.T @ U[i])

        print(U, "\n")
        print(V.T, "\n")
        print(U @ sigma @ V.T, "\n")






A = np.array([
    [3, 2, 2],
    [2, 3, -2],
])

# A = np.array([
#     [3, 2],
#     [2, 3],
#     [2, -2]
# ])

# A = np.array([
#     [3, 2, 1],
#     [2, 3, 1],
#     [2, -2, 1]
# ])

# npU, npSigma, npVT = np.linalg.svd(A)
# U, S, VT = svd(A)

# print("U: \n", U, "\n")
# print("npU: \n", npU, "\n")
# print("E: \n", S, "\n")
# print("npE: \n", npSigma, "\n")
# print("VT: \n", VT, "\n")
# print("npVT: \n", npVT, "\n")
# print("Result: \n", np.round(U @ S @ VT, 0))
# print("npResult: \n", np.round(npU @ S @ npVT, 0))

svd(A)

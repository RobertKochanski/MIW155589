import numpy as np
from numpy.linalg import eigh, norm


#  A  =  U  *  S  *  VT
# mxn = mxm * mxn * nxn

def svd(A):
    m, n = A.shape
    ev, V = eigh(A.T @ A)
    u = []
    U = np.zeros((m, m))
    VT = np.zeros((n, n))

    if m < n:
        for x in range(m):
            u.append(A @ V[:, x] / norm(A @ V[:, x]))

        for i in range(m):
            U[i] = u[i]

        U = U.T

        for j in range(n):
            VT[j] = V[:, j]

        S = np.round(U.T @ A @ V, 10)

    else:
        for x in range(n):
            u.append(A @ V[:, x] / norm(A @ V[:, x]))

        for i in range(n):
            U[i] = u[i]

        U = U.T

        for j in range(n):
            VT[j] = V[:, j]

        S = np.round(U.T @ A @ V, 10)

    return U, S, VT


A = np.array([[1, 1],
             [1, 3]])

# A = np.array([[1, 1, 0],
#              [1, 3, 1],
#              [0, 1, 1]])

# A = np.array([[1, 1],
#              [1, 0],
#              [4, 1]])

# A = np.array([[1, 1, 0],
#              [1, 5, 1]])

if A.shape[0] < A.shape[1]:
    A = A.T
    u, s, vt = svd(A)
    A = A.T
    print("A:", A, sep="\n")
    print("\nU * E * VT: \n", np.round(u @ s @ vt, 0).T)
else:
    u, s, vt = svd(A)
    print("A:", A, sep="\n")
    print("\nU * E * VT: \n", np.round(u @ s @ vt, 0))



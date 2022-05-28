import numpy as np
import math
# 18.05

BT = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, -1, -1, -1, -1],
    [1, 1, -1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, -1, -1],
    [1, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, -1]
], dtype=float)

B = BT.T

# sprawdzenie czy wektory macierzy sa ortogonalne (prostopadle do siebie)
ortogonalna = BT @ B

print(B, "\n")
print(BT, "\n")
print(ortogonalna, "\n")


# znormalizowanie wektorow (sprowadzenie do macierzy jednostkowej)
ortonormalna = ortogonalna.copy()
for i in range(len(ortogonalna)):
    ortonormalna[i] = ortogonalna[i] / math.sqrt(ortogonalna[i].T @ ortogonalna[i])

print(ortonormalna, "\n")


BT_norm = BT.copy()
for i in range(len(BT_norm)):
    BT_norm[i] = BT_norm[i] / math.sqrt(BT_norm[i].T @ BT_norm[i])

print(np.round(BT_norm, 0) + 0, "\n")

print(BT @ np.array([8, 6, 2, 3, 4, 6, 6, 5]))
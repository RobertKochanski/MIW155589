import math
import numpy as np

# ZADANIA
# W oparciu o operacje wektorowe proszę napisać funkcję do obliczania
# średniej arytmetycznej oraz wariancji i odchylenia standardowego


def srednia(wektor):
    wektor1 = np.ones(len(wektor))
    return np.dot(wektor, wektor1) / len(wektor)


def wariancja(wektor):
    sr = srednia(wektor)
    wektor_srednich = sr * np.ones(len(wektor))
    wektor_1 = wektor - wektor_srednich
    return np.dot(wektor_1, wektor_1)/len(wektor)


def odchylenie_standardowe(wektor):
    return math.sqrt(wariancja(wektor))


wektor = np.array([5, 3, 5])
print("Średnia: ", srednia(wektor))
print("Wariancja: ", wariancja(wektor))
print("Odchylenie standardowe: ", odchylenie_standardowe(wektor))
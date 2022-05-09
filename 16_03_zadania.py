import math
from collections import defaultdict


def load_file(file):
    lista = []
    with open(file, 'r') as file:
        for line in file:
            lista.append(list(map(lambda e: float(e), line.replace('\n', '').split())))
    return lista


def metryka_euklidesowa(listaA, listaB):
    wynik = 0
    for i in range(len(listaA) - 1):
        wynik += (listaA[i] - listaB[i]) ** 2
    return math.sqrt(wynik)


def zad1(x, lista):
    wynik = []
    for linia in lista:
        kd = linia[-1]
        odleglosc = metryka_euklidesowa(x, linia)
        wynik.append((kd, odleglosc))
    return wynik


lista = load_file('australian.dat')
x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(zad1(x, lista))


def zad2(lista):
    wynik = {}
    for item in lista:
        if not wynik.__contains__(item[0]):
            wynik[item[0]] = []
        wynik[item[0]].append(item[1])
    return wynik


print(zad2(zad1(x, lista)))


def zad3(x, lista, k):
    slownik = defaultdict(list)
    slownik_finalny = {}
    for i in range(len(lista)):
        klasa_decyzyjna = (lista[i][len(lista[0]) - 1])
        odleglosc = metryka_euklidesowa(x, lista[i])
        slownik[klasa_decyzyjna].append(odleglosc)
    for key in slownik:
        suma = 0
        slownik[key].sort()
        for i in range(k):
            suma += slownik[key][i]
        slownik_finalny[key] = suma
    return slownik_finalny


arr = load_file('australian.dat')
print(zad3([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], arr, 5))

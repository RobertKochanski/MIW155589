# pd
# lista składa się z inych list
# y = lita[0]
# pierwszy wiersz to y
# d(y,x), gdzie x należy do listy bez elementu z indeksem 0
# słownik, gdzie klucz to klasa decyzyjna x(ostani element to wniosek), a wartość to lista z odległościami
# {0 : lista z odleglosciami , 1: [], }

import math


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


def pracadomowa(lista):
    list_0 = []
    list_1 = []
    list_idx_0 = lista[0]
    for i in range(1, len(lista)):
        metryka_eukl = metryka_euklidesowa(list_idx_0, lista[i])
        if lista[i][len(lista[0]) - 1] == 0:
            list_0.append(metryka_eukl)
        elif lista[i][len(lista[0]) - 1] == 1:
            list_1.append(metryka_eukl)
    dictionary = {
        '0': list_0,
        '1': list_1,
    }
    return dictionary


arr3 = load_file('australian.dat')
dir = pracadomowa(arr3)
# print(dir)
print()
print(dir.get('1'))
print(dir.get('0'))
print(len(arr3))

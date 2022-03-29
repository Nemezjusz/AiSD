import numpy as np
from array import array
lista = [1, 2]
ar = array("f", [1, 2])


def funkcja_listowa(lista):
    x = list[-1] + list[-2]
    y = list[-1] - list[-2]
    list.append(x/y)
    if len(lista) <= 48:
        funkcja_listowa(lista)


def funkcja_tablicowa(ar):
    x = ar[-1] + ar[-2]
    y = ar[-1] - ar[-2]
    ar.append(x/y)
    if len(ar) <= 48:
        funkcja_tablicowa(ar)


funkcja_tablicowa(ar)
funkcja_listowa(lista)
print(lista)
print("średnia: ", np.average(lista))
print("mediana: ", np.median(lista))

l2 = []
for x in lista:
    if lista.count(x) > 1:
        l2.append(x)

if l2:
    print("powtórki", l2)
else:
    print("powtórki: puste")
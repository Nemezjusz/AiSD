dzrzewo = [1.5, [1.3, 1.6], 3.5, [3.7], 4.5, [4.0, 4.99], 7.5, [7.3, 7.8, [7.7, [7.6], 7.9]], 9.5, [9.3]]


def printing(lista, lvl=0):
    i = 0
    for x in lista:
        if type(x) == float:
            if i % 2 == 1 or lvl == 0:
                print("")
                if lvl > 0:
                    print(lvl * "\t", end="")
            print(lvl * "-", end="")
            print(x, end="")
            i += 1
        elif type(x) == list:
            printing(x, lvl+1)



def MIN(lista, korzen, lvl=0):
    global mm
    if mm == 99:
        p = lista.index(korzen)
        lista = lista[p:p + 2]

    for x in lista:
        if type(x) == float:
            if x < mm: mm = x
        else:
            MIN(x, 0, lvl=lvl + 1)

    return mm


def MAX(lista, korzen, lvl=0):
    global mx
    if mx == 0:
        p = lista.index(korzen)
        lista = lista[p:p+2]

    for x in lista:
        if type(x) == float:
            if x > mx: mx = x
        else:
            MAX(x, 0, lvl=lvl+1)

    return mx


def SEAR(lista, liczba):
    for x in lista:
        if type(x) == float:
            if x == liczba:
                return True
        elif type(x) == list:
            SEAR(x, liczba)



mx = 0
mm = 99
print(MAX(dzrzewo, 7.5))
print(MIN(dzrzewo, 7.5))

p = [1.5, [1.3, 1.6]]
print(p)
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


def INS(lista, liczba, lvl=0):
    if lvl>0:
        lista = [lista]
    if len(lista) == 1:
        lista.append([])

    if len(lista[1]) == 2:
        if liczba < lista[0]:
            INS(lista[1][0], liczba, lvl+1)
        else:
            pass

    elif liczba > lista[0] and len(lista[1]) != 0:
        lista[1].insert(1, liczba)
    else:
        lista[1].insert(0, liczba)

    print(lista)

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


def pom(krz, lista):
    if krz not in lista:
        i = 0
        while lista[i] < krz:
            if type(lista[i]) == float:
                i += 2
        lista.insert(i, krz)
        lista.insert(i+1, [])
    else:
        i = lista.index(krz)

mx = 0
mm = 99
print(MAX(dzrzewo, 7.5))
print(MIN(dzrzewo, 7.5))

p = [1.5, [1.3, 1.6]]
INS(p, 1.7)
print(p)
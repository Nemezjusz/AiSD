import random, math, numpy as np

def kolo(x):
    r = 1
    return math.sqrt(r**2 - x**2)

#poczatek >= 0
#koniec > poczatku

def MonteCarlo(poczatek, koniec, dokladnosc, funkcja):
    trafione = 0
    wszystkie = 0

    najmniejsza = funkcja(poczatek)
    najwieksza = funkcja(poczatek)

    for x in np.arange(poczatek, koniec+0.01, 0.01):
        if funkcja(x) > najwieksza:
            najwieksza = funkcja(x)
        if funkcja(x) < najmniejsza:
            najmniejsza = funkcja(x)

    while dokladnosc > wszystkie:
        y = random.uniform(najmniejsza, najwieksza)
        x = random.uniform(poczatek, koniec)
        if funkcja(x) >= y:
            trafione+=1
        wszystkie+=1

    p = (trafione/dokladnosc) * ((koniec-poczatek)*(najwieksza-najmniejsza))
    return p

#dla koła warotsc "r" jest rowna watrosci "koniec"
#aby funkcja działała poprawnie i zachowała swoja uniwersalnosc
#nalezy zmodyfikowac takze wartos "r" w funkcji koło

print("Sinus: ", MonteCarlo(0, 2, 100000, math.sin))
print("Koło (r=1): ", 4*MonteCarlo(0, 1, 100000, kolo))

def hanoi(n, poczatkowy, dodatkowy, docelowy):
    if n > 0:
        hanoi(n - 1, poczatkowy, docelowy, dodatkowy)
        docelowy.insert(0, poczatkowy.pop(0))
        hanoi(n - 1, dodatkowy, poczatkowy, docelowy)


poczatkowy = [1, 2, 3]
docelowy = []
dodatkowy = []

def hanoli_it(n, poczatkowy, dodatkowy, docelowy):

    if n % 2  == 0:
        przesuniecie = 2
    else:
        przesunecie = -2

    wieze = {
        0: poczatkowy,
        1: dodatkowy,
        2: docelowy
    }


    while len(poczatkowy) != 0 or len(dodatkowy) != 0:

        nieczynny = (nieczynny + przesuniecie) % 3
        czynne = [0,1,2]
        czynne.remove(nieczynny)

        try:
            if wieze[czynne[0]][0] < wieze[czynne[1]][0]:
                wieze[czynne[1]].insert(0, wieze[czynne[0]].pop(0))
            else:
                wieze[czynne[0]].insert(0, wieze[czynne[1]].pop(0))
        except IndexError:
            if len(wieze[czynne[1]]) == 0:
                wieze[czynne[1]].insert(0, wieze[czynne[0]].pop(0))
            else:
                wieze[czynne[0]].insert(0, wieze[czynne[1]].pop(0))

hanoli_it(3, poczatkowy, dodatkowy, docelowy)
print(docelowy)
from pathlib import Path
import math
path = Path("TSP.txt")
path = path.read_text()
path = path.splitlines()

miasta = []
for line in path:
    line = line.split("\t")
    line = [float(x) for x in line]
    line[0] = int(line[0])
    miasta.append(line)


def odleglosc(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def sciezka(miasta, poczatek):
    odl = 0
    sci = []
    pom = [poczatek+1]
    poprzedni = poczatek
    while len(sci)<99:
        tabela_odleglosci = []
        for miasto in miasta:
            if miasto[0] in pom:
                continue
            tabela_odleglosci.append([odleglosc(miasta[poprzedni][1], miasta[poprzedni][2], miasto[1], miasto[2]), miasto[0]])

        tabela_odleglosci.sort()
        sci.append((miasta[poprzedni][0], tabela_odleglosci[0][1]))
        odl += tabela_odleglosci[0][0]
        pom.append(tabela_odleglosci[0][1])
        poprzedni = tabela_odleglosci[0][1]-1

    print(odl)
    return sci

print(sciezka(miasta, 0))
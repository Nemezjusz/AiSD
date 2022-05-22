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
    sci = []
    odl = 0
    poprzedni = poczatek
    for x in range(0, len(miasta)):
        if x == poczatek:
            continue

        odl += odleglosc(miasta[poprzedni][1], miasta[poprzedni][2], miasta[x][1], miasta[x][2])
        sci.append((miasta[poprzedni][0], miasta[x][0]))
        poprzedni = x

    print("Odległość: ", odl)
    return sci

sc = sciezka(miasta, 4)
print(sc)
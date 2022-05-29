from pathlib import Path
import math

path = Path("packages20.txt")
path = path.read_text()
path = path.splitlines()
path = path[2:]

przedmioty = []
for line in path:
    line = line.split(",")
    line = [int(x) for x in line]
    wielkosc = line[1] * line[2]
    oplacalnosc = line[3] / wielkosc
    line.append(oplacalnosc)
    przedmioty.append(line)

przedmioty.sort(key=lambda x: x[4])
przedmioty.reverse()
print(przedmioty)

pojemonosc = 400
plecak = []
for przedmiot in przedmioty:
    wielkosc = przedmiot[1] * przedmiot[2]
    if pojemonosc > wielkosc:
        pojemonosc -= wielkosc
        plecak.append(przedmiot)
    else:
        break

print(plecak)
print(pojemonosc)

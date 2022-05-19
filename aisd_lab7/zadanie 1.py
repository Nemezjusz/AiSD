from pathlib import Path
from time import time
path = Path("1000_pattern.txt")
path = path.read_text()
path = path.splitlines()
lista = []

start = time()
for x in range(1000):
    for y in range(1000):
        try:
            if path[x][y] == "A" and path[x][y+1] == "B" and path[x][y+2] == "C" and \
                    path[x+1][y] == "B" and path[x+2][y] == "C":
                lista.append((x, y))
        except IndexError:
            pass
stop = time()
print(f"Rozmiar {len(path)}")
print(f"Czas: {stop-start}")
print(lista)
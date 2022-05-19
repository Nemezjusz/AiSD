from pathlib import Path
from time import time

path = Path("1000_pattern.txt")
path = path.read_text()
path = path.splitlines()


def haszing(arr, q):
    p = []
    for x in arr:
        if x.isdigit():
            p.append(x)
        else:
            p.append(str(ord(x)))

    p = "".join(p)
    return int(p) % q


wzor = ["A", "B", "C", "B", "C"]
hsz = haszing(wzor, 99)
lista = []

start = time()
for x in range(1000):
    for y in range(1000):
        try:
            p = [path[x][y], path[x][y + 1], path[x][y + 2], path[x + 1][y], path[x + 2][y]]
            t = haszing(p, 99)
            if t == hsz:
                if path[x][y] == "A" and path[x][y + 1] == "B" and path[x][y + 2] == "C" and \
                        path[x + 1][y] == "B" and path[x + 2][y] == "C":
                    lista.append((x, y))
        except IndexError:
            pass

stop = time()
print(f"Rozmiar {len(path)}")
print(f"Czas: {stop-start}")

print(lista)


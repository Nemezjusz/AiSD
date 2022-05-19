from time import time
l = int(input("Liczba krążków: "))
poczatkowy = [x for x in range(1, l+1)]

docelowy, dodatkowy = [], []
zamiana = 0

def hanoi(n, poczatkowy, dodatkowy, docelowy):
    global zamiana
    if n > 0:
        hanoi(n - 1, poczatkowy, docelowy, dodatkowy)
        print(f"Zamiana z {poczatkowy} na {docelowy}")
        docelowy.insert(0, poczatkowy.pop(0))
        print(f"Stan wiez po zmianie {poczatkowy},{dodatkowy}, {docelowy}")
        zamiana += 1
        hanoi(n - 1, dodatkowy, poczatkowy, docelowy)


start = time()
hanoi(l, poczatkowy, dodatkowy, docelowy)
stop = time()

print(f"ilość zmian: {zamiana}")
print(f"Czas {stop-start}")
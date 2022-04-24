def hanoi(n, poczatkowy, dodatkowy, docelowy):
    if n > 0:
        hanoi(n - 1, poczatkowy, docelowy, dodatkowy)
        docelowy.insert(0, poczatkowy.pop(0))
        hanoi(n - 1, dodatkowy, poczatkowy, docelowy)


poczatkowy = [1, 2, 3]
docelowy = []
dodatkowy = []
hanoi(3, poczatkowy, dodatkowy, docelowy)
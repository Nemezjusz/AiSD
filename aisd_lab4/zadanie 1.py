import random as r
from time import time
import numpy


def insertions(A):
    for i in range(len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = x

    return A


def mergesort(lista):
    if len(lista) > 1:
        r = len(lista) // 2
        L = lista[:r]
        M = lista[r:]

        mergesort(L)
        mergesort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            lista[k] = M[j]
            j += 1
            k += 1


# nlogn
czasy_ins = []
czasy_mrg = []
for y in range(10**2):
    L = []
    M = []

    for x in range(10**4):
        L.append(r.randint(0, 99))

    M = L.copy()

    start_ins = time()
    insertions(L)
    end_ins = time()
    czasy_ins.append(end_ins-start_ins)

    start_mrg = time()
    mergesort(M)
    end_mrg = time()
    czasy_mrg.append(end_mrg-start_mrg)

print("Srednia Ins: ", numpy.average(czasy_ins))
print("Maksimum Ins: ", numpy.max(czasy_ins))
print("Minimum Ins: ", numpy.min(czasy_ins))

print("\n")

print("Srednia Mgr: ", numpy.average(czasy_mrg))
print("Maksimum Mgr: ", numpy.max(czasy_mrg))
print("Minimum Mgr: ", numpy.min(czasy_mrg))
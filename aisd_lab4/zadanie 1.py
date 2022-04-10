def insertions(A):
    for i in (range(len(A))-1):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j+i] = A[j]
            j -= 1
        A[j+1] = x

    return A
#n^2


def merge(T, a, c, b):
    pass


def mergesort(A, a, b):
    if a < b:
        c = (a+b)/2
        mergesort(A, a, c)
        mergesort(A, c+1, b)
        merge(T, a, c, b)

#nlogn
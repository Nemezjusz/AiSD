lista = [2]

try:
    for x in range(3):
        lista[x]
except IndexError:
    print("problem z indeksem")

try:
    x = lista[0]/0
except ZeroDivisionError:
    print("nie dzieli sie przez 0")

try:
    fajna_uczelnia = a+g+h
except NameError:
    print("jest to kłamstwo")
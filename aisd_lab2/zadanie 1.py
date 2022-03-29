w = []
for x in range(500, 3001):
    if x % 7 == 0 and x % 5 != 0:
        w.append(str(x))


w = "".join(w)
print("String przed zamiana:", w)
print('Ilość "21": ', w.count("21"))
w = w.replace("21", "XX")
print('String po zamianie "21" na XX: ', w)
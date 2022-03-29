lista_numerow = range(1, 10)

#sposob z CPP
y = 0
for x in range(9):
    y += lista_numerow[x]
print(y)

#sposob iterowany
y = 0
for x in lista_numerow:
    y += x
print(y)
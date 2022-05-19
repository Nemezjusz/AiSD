from pathlib import Path

path = Path("1000_pattern.txt")
path = path.read_text()
path = path.splitlines()
arr = "AB13FES"


def haszing(arr):
    arr = list(arr)
    for x in arr:
        try:
            pass
        except:
            x = ord(x)

print(haszing(arr))

for x in range(1000):
    for y in range(1000):
        pass

print(14152 % 13)
print(8 % 13)
print(31415 % 13)

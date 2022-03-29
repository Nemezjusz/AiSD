import os, string, shutil

cwd = os.getcwd()
path = os.path.join(cwd, "zadanie1-Rozwiazanie")
path2 = os.path.join(cwd, "zadanie1")
litery = list(string.ascii_uppercase)

try:
    os.mkdir(path)
    pliki = os.listdir(path2)

    for litera in litery:
        os.mkdir(os.path.join(path, litera))

    for plik in pliki:
        for folder in os.listdir(path):
            if str(plik)[0] == str(folder)[0]:
                shutil.copy(os.path.join(path2, plik), os.path.join(path, folder))

    for folder in os.listdir(path):
        if len(os.listdir(os.path.join(path, folder))) == 0:
            os.rmdir(os.path.join(path, folder))

except FileExistsError:
    print("plik juz istnieje")
from time import time
while True:
    słowo = input("Czy słowo ... znajduje sie w SJP? : ")
    słowo = słowo.lower()
    if len(słowo.split(" ")) > 1:
        print("Nie jest to pojedyncze słowo!")
    else:
        break

start = time()
with open("SJP.txt", "r", encoding='utf8') as sjp:
    r_sjp = sjp.read()
    sjp = r_sjp.splitlines()
    if słowo in sjp:
        print("Słowo znajduje sie w SJP!")
    else:
        print("Słowo NIE znajduje sie w SPJ")

stop = time()
print("Czas przetwarzania: ", stop-start)
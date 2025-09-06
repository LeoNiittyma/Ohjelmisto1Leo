import random

summa = 1

maara = int(input("Arpakuutioiden lukumäärä: "))


for i in range(maara):
    plus = random.randint(1, 6)
    summa = summa + plus

print(f"Silmälukujen summa on", summa)
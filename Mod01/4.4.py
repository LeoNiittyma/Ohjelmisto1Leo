import random


numero = random.randint(1,10)

arvaus = float(input("Syötä luku: "))

while arvaus != numero:
    if arvaus > numero:
        print("Liian suuri arvaus!")
        arvaus = float(input("Syötä luku: "))
    elif arvaus < numero:
        print("Liian pieni arvaus!")
        arvaus = float(input("Syötä luku: "))
print("Oikein!")
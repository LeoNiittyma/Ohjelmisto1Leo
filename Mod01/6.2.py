import random

maksimi = int(input("Anna nopan maksimisilmäluku: "))

def nopanheitto():
    return random.randint(1,maksimi)

def numero():
    tulos = 0
    while tulos != maksimi:
        tulos = nopanheitto()
        print(tulos)
    return tulos

numero()
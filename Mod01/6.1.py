import random

def nopanheitto():
    return random.randint(1,6)

def numero():
    tulos = 0
    while tulos != 6:
        tulos = nopanheitto()
        print(tulos)
    return tulos

numero()
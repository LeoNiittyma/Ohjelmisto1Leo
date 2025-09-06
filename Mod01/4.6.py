import random

pisteet = int(input("Syötä pisteiden lukumäärä: "))

p = 0

for i in range(pisteet):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    print(f"Arvottu piste: {x}, {y}")

    if x**2 + y**2 < 1:
        p = p + 1

pi = 4 * p / pisteet

print(f"Pi-in likiarvo {pisteet} pisteellä on noin {pi}")
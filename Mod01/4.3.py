luku_str = input("Syötä luku: ")

luku = float(luku_str)

isoin = luku
pienin = luku

while luku_str != "":
    luku_str = input("Syötä luku:")
    if luku_str == "":
        break
    luku = float(luku_str)
    if pienin > luku:
        pienin = luku
    if isoin < luku:
        isoin = luku

print(pienin)
print(isoin)
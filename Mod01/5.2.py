luvut = []

luku_str = input("Anna luku: ")

while (luku_str != ""):
    luku = float(luku_str)
    luvut.append(luku)
    luku_str = input("Anna luku: ")

luvut.sort(reverse=True)

print(luvut[0:5])
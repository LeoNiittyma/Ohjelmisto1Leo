def jako(luku):
    jaettu = luku / 3.875
    return jaettu

def kysely():
    maara = float(input("Anna gallonamäärä: "))
    while maara >= 0:
        print(jako(maara))
        maara = float(input("Anna gallonamäärä: "))
    return maara

kysely()

print("Annoit negatiivisen gallonamäärän!")
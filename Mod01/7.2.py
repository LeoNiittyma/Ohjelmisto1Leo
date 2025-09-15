nimilista = set()

nimi = input("Anna nimi:")
if nimi in nimilista:
    print("Aiemmin syötetty nimi")
else:
    print("Uusi nimi")
nimilista.add(nimi)

while nimi != "":
    nimi = input("Anna nimi:")
    if nimi in nimilista:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    nimilista.add(nimi)

for i in nimilista:
    print(i)
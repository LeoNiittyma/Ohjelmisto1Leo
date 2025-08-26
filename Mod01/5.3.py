kokonaisluku = int(input("Anna kokonaisluku: "))

alkuluku = True

if kokonaisluku >= 2:
    for i in range (2,kokonaisluku):
        if kokonaisluku % i == 0:
            alkuluku = False

    if alkuluku == True:
        print("Luku on alkuluku")
    else:
        print("Luku ei ole alkuluku")

else:
    print("Luku ei ole alkuluku")
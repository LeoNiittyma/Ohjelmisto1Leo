vuosi = float(input("Anna vuosi: "))

if vuosi % 4 == 0:
    print("Vuosi on karkausvuosi")
    if vuosi % 100 == 4:
        if vuosi % 400 == 0:
            print("Vuosi on karkausvuosi")

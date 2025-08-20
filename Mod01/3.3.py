sukupuoli = input("Anna sukupuolesi: ")
hemo = float(input("Anna hemoglobiiniarvosi: "))

if sukupuoli == "Mies":
    if hemo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemo > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

else:
    if hemo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemo > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
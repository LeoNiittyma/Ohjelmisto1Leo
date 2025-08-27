def yksikkohinta(halkaisija,hinta):
    laskettu =  hinta / halkaisija
    return laskettu

def pizzat():
    pizza1_hinta = int(input("Anna ensimmäisen pizzan hinta: "))
    pizza1_halkaisija = int(input("Anna ensimmäisen pizzan halkaisija: "))
    pizza2_hinta = int(input("Anna toisen pizzan hinta: "))
    pizza2_halkaisija = int(input("Anna toisen pizzan halkaisija: "))
    pizza1_tulos = yksikkohinta(pizza1_halkaisija,pizza1_hinta)
    pizza2_tulos = yksikkohinta(pizza2_halkaisija,pizza2_hinta)

    if pizza1_tulos < pizza2_tulos:
        print("Ensimmäisellä pizzalla saat enemmän vastinetta rahalle!")
    elif pizza2_tulos < pizza1_tulos:
        print("Toisella pizzalla saat enemmän vastinetta rahalle!")
    else:
        print("Saat molemmilla pizzoilla yhtä paljon vastinetta rahalle!")

pizzat()
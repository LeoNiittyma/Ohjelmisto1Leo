lista = {}

while True:
    kysymys = input(
    "Haluatko syöttää uuden lentoaseman, hakea jo syötetyistä lentoasemista vai lopettaa haun?: (Syöttää / Hakea / Lopettaa)"
    )
    if kysymys == "Syöttää":
        uusi_icao = input("Anna lentoaseman ICAO-koodi: ")
        uusi_nimi = input("Anna lentoaseman nimi: ")
        lista[uusi_icao] = uusi_nimi
    elif kysymys == "Hakea":
        haku = input("Anna lentoaseman ICAO-koodi: ")
        if haku in lista:
            print(f"ICAO-koodia {haku} vastaavan lentokentän nimi on {lista[haku]}")
        else:
            print("Et antanut jo syötettyä ICAO-koodia!")
    elif kysymys == "Lopettaa":
        break
    else:
        print("Väärä syöte!")


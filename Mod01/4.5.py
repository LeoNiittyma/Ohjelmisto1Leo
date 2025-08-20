salasana = "rules"
tunnus = "python"

tunnus_arvaus = input("Anna tunnus: ")
salasana_arvaus = input("Anna salasana: ")

arvaukset = 1

while tunnus_arvaus != tunnus or salasana_arvaus != salasana:
    tunnus_arvaus = input("Anna tunnus: ")
    salasana_arvaus = input("Anna salasana: ")
    arvaukset = arvaukset + 1
    if arvaukset == 5:
        if tunnus_arvaus != tunnus or salasana_arvaus != salasana:
            print("Pääsy evätty!")
            break

if tunnus_arvaus == tunnus and salasana_arvaus == salasana:
    print("Tervetuloa!")

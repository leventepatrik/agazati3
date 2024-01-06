def feladat1():
    Muzeum_neve = input("Kérem, adja meg a hét napját: ")
    Latogato_neve= input("Kérem, adja meg az óra nevét: ")

    ertek = input("Kérem, adja meg az értékelést (1-5): ")

    ertek = int(ertek)

    if 1 <= ertek <= 5:
            print("Köszönjük az értékelést!")
            print(f"A hét napja: {Muzeum_neve}\nÓra neve: {Latogato_neve}\nÉrtékelés: {ertek}")
    else:
            print("Hibás értékelés! Kérem, adjon meg egy értéket 1 és 5 között.")
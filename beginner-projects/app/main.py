people = []
while True:
    # zapíš meno
    x = input('Meno ? :')
    # over vek
    while True:
        try:
            y = int(input("Vek ? : "))
            break
        except ValueError:
            print("použi číslo prosím...")
    # over či zapísal ano
    def ano_nie():
        while True:
            z = input('Si programator ? "ano/nie"').lower()
            # # # # if z == "áno" or z == "ano":
            # # # #     return True
            if z in ["áno", "ano"]:
                    return True
            elif z == "nie":
                return False
            else:
                print("Zadaj len 'áno' alebo 'nie'.")

    zz = ano_nie()
    print(zz)
    vek = int(y)

    # print("\n--- Výsledok ---")
    # print(f"Meno: {x}")
    # print(f"Vek: {y}")
    # print(f"Je programátor: {zz}")


    osoba = {
        "meno" : x,
        "vek" : y,
        "programator" : zz
        
    }

    # def fun():
    #     text = ""
    #     for key,value in osoba.items():
    #         text += f"{key}: {value}\n"
    #     return text
    people.append(osoba)
    # # # # # # # # Aj takto sa to dá napísať cez join
    # def fun():
        # return "\n".join([f"{k}: {v}" for k, v in profil.items()])
            # Spýtaj sa, či chceš pokračovať
    dalsi = input("Chceš pridať ďalšiu osobu? (áno/nie): ").lower()
    if dalsi not in ["áno", "ano"]:
        break
    print("\n--- Všetci ľudia ---")
    for osoba in people:
         for kluc, hodnota in osoba.items():
            print(f"{kluc}: {hodnota}")
            print("-" * 20)

with open("ludia.txt", "w") as f:
    for osoba in people:
        for kluc, hodnota in osoba.items():
            f.write(f"{kluc}: {hodnota}\n")
        f.write("-" * 20 + "\n")

    # # with open("profil.txt", "w") as f:
    # #     f.write(fun())
    
    # # with open("profil.txt") as f:
    # #     print(f.read())
        

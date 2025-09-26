from gui import open_window,otvor_gui


# open_window()
vek = open_window()
# print (vek)
svek = []
dvek = []
while True: 
    vek = open_window()
    x = vek
        # x = input("napíš svoj vek : ")
    if x is None or x.lower() == ("koniec"):
            break
    try:
        x = int(x)
        if x >= 18 :
            svek.append(x)
        if x <= 18 :
            dvek.append(x)
        # vek.append(x)
    except ValueError:
            print("prosím zadaj číslo ! :")
            break
print(f"dosípelí({len(svek)}): {sorted(svek)}\n")
print(f"Deti:({len(dvek)}){dvek}\n")
from gui import otvor_gui

# meno = f"dosípelí({len(svek)}): {sorted(svek)}\n"
vysledok = f"Dospelí({len(svek)}): {sorted(svek)}\n Deti({len(dvek)}): {sorted(dvek)}"
otvor_gui(vysledok)  # posielame výsledok ako text

     
# print(vek_entry)
# from gui import open_window
# open_window()

svek = []
dvek = []
while True : 
        x = input("napíš svoj vek : ")
        if x.lower() == ("koniec"):
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

print(f"dosípelí({len(svek)}): {sorted(svek)}\n")
print(f"Deti:({len(dvek)}){dvek}\n")
     
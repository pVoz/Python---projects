import math

# jedna plechovka = 5m štvorcových 
h = int(input("Výška steny : "))
l = int(input("Šírka steny : "))
# zaokruhlovať hore 

# h = int(h)
# l = int(l)
plechovka = 5
def vypocet(hight,lenght):
    result = hight * lenght
    result = result / plechovka
    return math.ceil(result)
    # math.ceil(result)

vysledok = vypocet(h,l)

if vysledok == 1 :
    nazov = "plechovku"
else:
    nazov = "plechoviek "

# print(vypocet(h,l))
print(f"\nPotrebuješ {vysledok} {nazov} farby na stenu. \n")
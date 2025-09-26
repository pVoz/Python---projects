import math 
osoba =  {
        "meno": "Peter",

        "vek": 31,

        "je_programator": True
}

for i in osoba.values():
    print(i)


vek = int(osoba["vek"])
# print(vek)print("\n")
print("\n")


if vek < 18 :
    print("si neplnoletý")
else : 
    print("si plnoletý")
    print("\n")

numb= [1,2,3,4,5]
k = 10 
for c in [x * 10 for x in numb]:
    print(c)
print("\n")


for key,value in osoba.items():
    print(f"{key}:{value}")

print("\n")


quit()

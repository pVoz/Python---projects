
osoba = {
    "meno": "Peter",
    "vek": 31,
    "mesto": "Bratislava"
}

# print(list(osoba))
for i in osoba.values():
    print(i)

osoba["okres"] = "BB"

# # print(list(osoba))
# for i in osoba.values():
#     print(i)

# x= osoba.items()
# print(x)


for key,value in osoba.items():
    print(f"{key}:{value}")
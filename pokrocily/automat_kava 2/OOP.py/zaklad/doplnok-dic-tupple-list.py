

# String
print("Nazdar")
long_string = '''
    adsadasda
    asdasdsad
    asdas
    asd
    a
    sd
    asdasdasd

'''
print(long_string)


# Escape sequence
info = 'it\'mine'
tabulator = "text \t asdkasldja"
print(tabulator)


# FORMATOVANÝ STRING
name = "Peter"
age = 32
print("ahoj {}. Starý som {}".format(name,age))
print("ahoj {0}. Starý som {1}".format(name,age))

# PRáca so stringom 
name = "testovanie"
       #0123456789
print(name[0])
# [start:stop]
print(name[0:4])
# [start:stop:krok]
print(name[0:4:2])
# Kombinacia
print(name[1:])
print(name[:5])
print(name[-1])
print(name[::-1])



# Immutability = nemennosť
my_name = "Peter"


# Metody a funkcie

# Fubkcia
print(len(my_name))
print(abs(-7))

# Metody
print(my_name.upper())

# Password
print("*" * len(name))


# Slicing
to_do = [
    "nakrmit psa",
    "isť do obchodu",
    "spať",
    "praca"
]
# print(to_do[0::1])
to_do[0] = "vonku ? " 
print(to_do[0::1])

# POZOR
to_do2 = to_do
to_do2[0] = "super nový ukol"
print(to_do)
print(to_do2)

# Skopirovanie listu do nového 
to_do3 = to_do[:] #[:]-> skopirovanie celý listu 
# alebo 
to_do4 = to_do.copy() # --> skopiruje celý list
to_do3[0] = "nerob nič "
print(to_do3)

# MATRIX - 2 dimenzionalny list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])
print(matrix[1][0])
print(matrix[2][1])
print(matrix[2][2])

to_do = [
    "nakrmit psa",
    "nakrmit mačku",
    "nakrmit škrečka"
]
to_do.append("Nakrmit Hada")
to_do.insert(1,"Nakrmit Vtačika")
to_do.extend(["nakrmit zajaca", "nakrmit pythona"])


# to_do.clear() --> vyčistí celý list
# to_do.pop() --> odstraní posledný prvok
# to_do.pop(0) --> odstraní špecific prvok
# to_do.remove("nakrmit psa")
print(to_do)


# List Unpacking 
to_do4 = [
    "nakrmit mačku",
    "vyvenčit psa",
    "urobit jedlo",
    "absolvovať lekarsku prehliadku ",
    "vymalovať izbu",
    "kupit nový telefón"
]

a, b, c, d, e, f = to_do4
print(b)

a, *rest, g = to_do4
print(rest)


# Dictionary .. 
book = {
    "title": "Harry Potter a kámen mudrcú",
    "author": "J. K. Rowling",
    "year": 1997
}
# # print(book["title"])
print("Aaa--a-a--a-aa--a-a-a-a--a-a-a-")
# print("year" in book.keys()) 
# print(1997 in book.values()) 
print(book.items())
print("- - - - - - - - - - - - - - - - - - - - - - - ")
# zmení položku key = value , updatuje(ked nemáš prístup ku zdroju )
book.update({"year": 1998})
print(book)

print("- - - - - - - - - - - - - - - - - - - - - - - ")
# Tupple 
firest_tuple = (0, 1, 2, 3, 4, 5)
print(3 in firest_tuple)
print("- - - - - - - - - - - - - - - - - - - - - - - ")

colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    (0, 1): (1, 0, 0),
    "blue": (0, 0, 255)
}
# print(colors["red"])
print(colors[(0,1)]) 

first_tupple = ("a", "b", "c", "d")

# Metody
print(first_tupple.count("c")) # 3
print(first_tupple.index("b")) # 1


# SET -> unikatne , nezoradené hodnoty
my_name = "petervzr"
my_set = set(my_name) # unikátne hodnoty vyberie (neopakuje hodnoty ako "e"2x a pod. a nezoradí ich )
# print(my_set)

old_set = my_set.copy() # skopíruje pôvodný set 
my_set.add("c")
print(my_set)
print(old_set)
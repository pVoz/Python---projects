
# name = "Peter"         # str
# vek = 14               # int
# vyska = 182.4          # float
# si_programator = True  # bool

# print(name, type(name). __name__)
# print(vek, type(vek). __name__)
# print(vyska, type(vyska). __name__)
# print(si_programator, type(si_programator). __name__)

# # === START_KODU ===

x = input('Enter your name:')
y = int(input('Age:'))
vek = int(y)

    # Funkcia 
# def roky (vek):
#     vysledok= vek+100 
#     return vysledok   
 
# vysledok = roky(vek)

# print(f"{vysledok}")   
    
rozdiel= 50 - vek
if vek <= 0 :
    print("zadal si neplatný vek ")
elif vek <= 18 :
    print("Si ešte dieťa")
    
elif vek >= 65 :
        print("Si už dôchodca")
else :
     print("si dospelý")
     
     

for i in range(10):
    print(i)
    i = 1
    
c = 5
while c < 6:
  print(c)
  c += 1

s = "hello"

for char in x:
    print(char)
    
    


def pozdrav(x):
    # telo funkcie
    print(f'Nazdar , ako sa máš  {x} ?')

pozdrav(x)  # zavolanie


# print(rozdiel)
print(f"Hello, {x}, máš {vek} rokov.")
print("Chýba ti" , rozdiel  ,"rokov do päťdesiatky.")

# print(type(vek))
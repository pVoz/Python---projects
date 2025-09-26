import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

# for letter in random(letters(1,100)):
lt = input("Koľko písmen ? ")
ns = input("Koľko čisiel ? ")
sc = input("Koľko znakov ? ")

let_ran = random.sample(letters, int(lt)) # zo zoznamu vráti  počet náhodných písmen
# print(let_ran)  # 
num_ran = random.sample(numbers, int(ns)) # zo zoznamu vráti  počet náhodných písmen
# print(num_ran)  # 
spc_ran = random.sample(special_char, int(sc)) # zo zoznamu vráti  počet náhodných písmen
# print(spc_ran)  # 



# for letter in random.choice(letters(lt)):
#     print(letter)
#     letter
#     # print(list(letters))
# for number in random.choice(numbers):
#     # print(number)
#     number
# for spec in random.choice(special_char):
#     # print(spec)
#      spec

x = ''.join(i[0] for i in let_ran)
print(x)  # Výstup: abcdf

y = ''.join(i[0] for i in num_ran)
print(y)  # 

z = ''.join(i[0] for i in spc_ran)
print(z)  # 

s_ran = x , y ,z
print(s_ran)

# j = [x,y,z]
vysledok = ''.join(i for i in s_ran)
# print(vysledok)  # Výstup: ab

znaky = list(vysledok)       # krok 1: premena na zoznam
random.shuffle(znaky)    # krok 2: premiešanie
vysledok2 = ''.join(znaky)  # krok 3: späť na reťazec

print(vysledok2)


# random.shuffle(s_ran)
# print (s_ran)
# j = ''.join(s_ran)
# print(j)
# # random.shuffle(str(x))

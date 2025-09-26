import random as rd
import os 

# Úvod do hry 
print("Vitaj v hre guess secret number , poraz počítač . ")


random_number = rd.randint(1,100)

def difficulty():
    difficulty = input("Zvol si obtiažnosť : Napíš 'easy' alebo 'hard'")
    if difficulty == "easy":
        return  10 
    elif difficulty == "hard":
        return 5
def guessing_game():
    
    attemps = difficulty()
        # print(random_number)
    another_game = ""
    while attemps > 0 : 
        
        guess_number = int(input("Zadaj hádané číslo : "))
        if guess_number > random_number :
            print("Príliš vysoké číslo ")
            attemps -= 1
        elif guess_number < random_number :
            print("Príliš nízke číslo ")
            attemps -= 1
        else : 
            print("Porazil si počítač , VYHRAL SI ! ")
            another_game = input("Napíš 'yes' ak chceš pokračovať ,napíš 'no' ak chceš hru ukončiť  :")
        if attemps == 0 :
            print("Prehral si , počítač vyhral ! ")
            another_game = input("Napíš 'yes' ak chceš pokračovať ,napíš 'no' ak chceš hru ukončiť  :")    
        if another_game == "yes":
            os.system("clear")
            guessing_game()
        elif another_game == "no":
            os.system("clear")
            break
        print(f"Váš počet pokusov na hádanie je {attemps}")
            
guessing_game()
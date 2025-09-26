from data import data
import random as rd
import os

score = 0

def check_answer(user, right_answer, score):
    if user == right_answer:
        score += 1
        print(f"Uhádol si, tvoje skóre je {score}")
        return score, True
    else:
        print(f"Zlá odpoveď, konečné skóre je {score}")
        return score, False

def printing_options(acc1, acc2):
    print(f"Porovnaj A : {acc1['name'], acc1['description'], acc1['country']}")
    print(f"Porovnaj B : {acc2['name'], acc2['description'], acc2['country']}")

while True:
    account1 = rd.choice(data)
    account2 = rd.choice(data)

    while account1 == account2:
        account2 = rd.choice(data)

    secreet1 = account1["follower_count"]
    secreet2 = account2["follower_count"]

    if secreet1 == secreet2:
        account2 = rd.choice(data)
        secreet2 = account2["follower_count"]

    if secreet1 > secreet2:
        right_answer = "A"
    else:
        right_answer = "B"

    # DEBUG: pre kontrolu
    print(f"DEBUG: A má {secreet1} followerov, B má {secreet2}")
    print(f"DEBUG: Správna odpoveď je: {right_answer}")

    printing_options(account1, account2)

    user_answer = input("Kto má viac followerov na Instagrame? Napíš A alebo B: ").upper()

    score, correct = check_answer(user_answer, right_answer, score)

    if not correct:
        input("Stlač Enter pre pokračovanie...")
        os.system("clear")  # ak si na Windows, zmeň na "cls"
        another_game = input("Chceš hrať od začiatku? Napíš 'yes' alebo 'no': ").lower()
        if another_game == "yes":
            score = 0
            continue
        else:
            print("Hra ukončená.")
            break

import random
from gui import stages
from names import words
#Hangman

# Vitanie v hre 
print("\nVitaj v hre Hangman , tvojou úlohou je uhádnuť postavu z filmu Harry Potter \n ")
# Generovanie náhodného slova 

random_word = words[random.randint(0,len(words)-1)]
# print (random_word)

# Generovanie podržníkov
hidden_word = []    
for one_letter in random_word:
    hidden_word.append("_")
# print (hidden_word)

# Životy
lives = 6


 # vypisanie slova s podtržitkami bez "list"
printedWord = ""
for one_letter in hidden_word:
    printedWord += one_letter
# print(printedWord)

    
while "_" in hidden_word:    
    guess = input("zadaj hádané písmeno : ").lower()
    for index in range(0, len(random_word)):
        if guess == random_word[index]:
            hidden_word[index] = guess

    # print(hidden_word)
    if guess not in random_word:
        lives -= 1
        print(str(stages[lives]))
    print (f"Počet tvojich životov je :{lives}")
    if lives == 0 :
        print(f"\n Prehral si....\n")
        break
    # vypisanie slova s podtržitkami bez "list"

    printedWord = ""
    for one_letter in hidden_word:
        printedWord += one_letter
    print(printedWord)

    # kontrola výťaztva„
    if "_" not in hidden_word:
        print("Vyhrál si ")
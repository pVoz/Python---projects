# y = input('Napíš zoznam kamarátov (oddelené čiarkou): ')
x = input('Napíš čísla od 1-10 (oddelené čiarkou): ')

# txt_zoz = y.split(",")               # rozdelenie textu na mená
cis_zoz = x.split(",")               # rozdelenie čísiel ako text

# print(cis_zoz)                       # vypíše zoznam čísel (ako texty)
# print(len(txt_zoz))                  # počet mien

# txt_zoz.append("orange")            # pridá meno "orange" do zoznamu

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# for i in txt_zoz:
#     print(i)
    
for i in cis_zoz:
    print(i)

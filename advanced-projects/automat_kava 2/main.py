from source_data import MENU
from source_data import resources

# print(MENU)
# print(resources)

# === Zakladné nastavenie ===
esspresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]


# === Funkcie ===


def report(data):
    print(f"Voda: {data["water"]}")
    print(f"Mlieko: {data["milk"]}")
    print(f"Káva: {data["coffee"]}")

def coins():
    print("Prosím vhodte mince 1, 2, 5, 10, 20, 50")
    kc1 = int(input("Koľko 1kč chcete vložit?: "))
    kc2 = int(input("Koľko 2kč chcete vložit?: ")) * 1
    kc5 = int(input("Koľko 5kč chcete vložit?: ")) * 5
    kc10 = int(input("Koľko 10kč chcete vložit?: ")) * 10
    kc20 = int(input("Koľko 20kč chcete vložit?: ")) * 20
    kc50 = int(input("Koľko 50kč chcete vložit?: ")) * 50
    suma = kc1 + kc2 + kc5 + kc10 + kc20 + kc50
    print(f"Celkom ste vložili {suma}")
    return suma

# Výpočet vložených penazí - cena nápoja

def calculate_change(user_sum_coins,price):
    refund = user_sum_coins - price
    if refund >= 0:
        print("Nápoj sa pripravuje. ")
        if refund > 0 :
            print(f"Vraciam naspať : {refund}")
    else:
        print(f"Nevhodili ste dostatok penez . Ješte je potrebné vhodit {price - user_sum_coins} Kč")

# vytiahnutie zdrojových údajov ( nepozmenit originálne )
def fill_in_ingredience():
    return resources

def consumption_ingredience(name_of_drink,ingredience):
        ingredience["water"] =  ingredience["water"] - MENU[name_of_drink]["ingredients"]["water"]      
        ingredience["milk"] =  ingredience["milk"] - MENU[name_of_drink]["ingredients"]["milk"]
        ingredience["coffee"] =  ingredience["coffee"] - MENU[name_of_drink]["ingredients"]["coffee"]      
        print(f"Ostatok ingrediencii : {ingredience}")

def calculate_ingredients(drink_name):
    if drink_name == "espresso":
        # rest_of_ingredience["water"] =  rest_of_ingredience["water"] - MENU["espresso"]["ingredients"]["water"]      
        # rest_of_ingredience["milk"] =  rest_of_ingredience["milk"] - MENU["espresso"]["ingredients"]["milk"]
        # rest_of_ingredience["coffee"] =  rest_of_ingredience["coffee"] - MENU["espresso"]["ingredients"]["coffee"]      
        # print(f"Ostatok ingrediencii : {rest_of_ingredience}")
        consumption_ingredience(drink_name, rest_of_ingredience)
        
    elif drink_name == "latte":
    #     rest_of_ingredience["water"] =  rest_of_ingredience["water"] - MENU["latte"]["ingredients"]["water"]      
    #     rest_of_ingredience["milk"] =  rest_of_ingredience["milk"] - MENU["latte"]["ingredients"]["milk"]              
    #     rest_of_ingredience["coffee"] =  rest_of_ingredience["coffee"] - MENU["latte"]["ingredients"]["coffee"] 
    #     print(f"Ostatok ingrediencii : {rest_of_ingredience}") 
        consumption_ingredience(drink_name, rest_of_ingredience)
    elif drink_name == "cappuccino":
    #     rest_of_ingredience["water"] =  rest_of_ingredience["water"] - MENU["cappuccino"]["ingredients"]["water"]             
    #     rest_of_ingredience["milk"] =  rest_of_ingredience["milk"] - MENU["cappuccino"]["ingredients"]["milk"]       
    #     rest_of_ingredience["coffee"] =  rest_of_ingredience["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"] 
    #     print(f"Ostatok ingrediencii : {rest_of_ingredience}") 
        consumption_ingredience(drink_name, rest_of_ingredience)
        
def ingredience_checker(in_water,in_milk,in_coffe):
    if in_water < 0:
        print("Nemáme dostatok ingrediencii na tento nápoj")
        return False
    elif in_milk < 0:
        print("Nemáme dostatok ingrediencii na tento nápoj")
        return False
    elif in_coffe < 0:
        print("Nemáme dostatok ingrediencii na tento nápoj")
        return False
    else:
        print("Na váš nápoj máme dostatok ingrediencii. ")    
        return True
    
# === Kód automatu ===
# Načitanie pôvodných ingrediencii
rest_of_ingredience = fill_in_ingredience()

lets_continue = True

while(lets_continue):    # Voľba uživatela 
    user_choice = input("Čo by si si dal/a ?(espresso/latte/cappuccino): ")
    # zapisanie orig.dat do premennej (ochrana)
    print(rest_of_ingredience)

    # Vypočitanie koľko ostáva ingrediencii
    calculate_ingredients(user_choice)

    # Kontrola dostatku ingrediencii !!    
    if user_choice != "report":
        lets_continue = ingredience_checker(rest_of_ingredience["water"],rest_of_ingredience["milk"],rest_of_ingredience["coffee"])
    
    # Kontrola ingrediencii
    if lets_continue == False:
        break
    
    # Kontrola reportu
    if user_choice == "report":
        report(rest_of_ingredience)
        
        
    # === Logika automatu ====
    
    if user_choice == "espresso":
        sum = coins()
        print (f"Cena esspresa je : {esspresso_price} Kč")
        calculate_change(sum,esspresso_price)
    elif user_choice == "latte" :
        sum = coins()
        print (f"Cena esspresa je : {latte_price} Kč")
        calculate_change(sum,latte_price)
    elif user_choice == "cappuccino":
        sum = coins()
        print (f"Cena esspresa je : {cappuccino_price} Kč")
        calculate_change(sum,cappuccino_price)

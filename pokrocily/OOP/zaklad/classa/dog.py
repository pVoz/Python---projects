class Dog:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

        
        
        
havo1 = Dog("Peso 1",14)
havo2 = Dog("Peso 2",22)
havo3 = Dog("Peso 3",10)
dogs = [havo1,havo2,havo3]

# Zisti ktorý pes je najstarší a vypíše jeho meno a vek 
def oldest(all_dogs):
    oldest_dog_age = 0
    oldest_dog_name = ""
    for one_dog in all_dogs:
        # print(one_dog.age)
        if one_dog.age > oldest_dog_age:
            oldest_dog_age = one_dog.age
            oldest_dog_name = one_dog.name
    return oldest_dog_age, oldest_dog_name
print(oldest(dogs))


# --- toto je ta ista funkcia : Zistenie najstaršieho psa ----
def oldestt(*args):
    return max(args)
            # TUPPLE___!!!!
result = oldestt(havo1.age,havo2.age,havo3.age)
print(result)
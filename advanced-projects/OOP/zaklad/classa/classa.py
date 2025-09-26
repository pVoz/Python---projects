

class WizardPlayer:
    # Constructor
    def __init__(self, name="anonym", age=0):
        # if age >= 18:
            self.name = name
            self.age = age
        
    def attack(self):
        return "Útok 1.Stupne"
        
    def age_checker(self):
        if self.age >= 18:
            print("Môžeš hrať ..")
        else:
            print("Nemôžeš hrať , tvoj vek je príliš nízky.")
        
class HeadWizard(WizardPlayer):
    # rozšírenie konštruktora o super ( dedí aj name aj age a je pridaný Type)
    def __init__(self, type, name, age):
         super().__init__(name, age)
         self.type = type
    
    def attack(self):
             return "Útok 2.Stupne!"       
    def avada_kedavra(self):
        return "Avada Kedavra"    
        
            
# user_name = input("Ake je tvoje meno ? ")
# user_age = int(input("Aký je tvoj vek ? "))

player1 = WizardPlayer("Peter", 34)
player2 = HeadWizard("good","Peter", 34)
# player1.age_checker()
# print(player2.attack())
# player1.attack()
# # help(player1)
#( ukazuje postupnosť hladania )

# Method resolutionb order = MRO  #( ukazuje postupnosť dedenia(hladania) )
print(HeadWizard.mro())
print(HeadWizard.__mro__)

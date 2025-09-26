class Robot:
    
    # Constructor
    def __init__(self, bateria, dlzka_ruk):
        self.bat = bateria
        self.del_ruk = dlzka_ruk
        self.ukony_do_kontroly = 365 # konštatná premenná 
    
    def krok_vpred(self):
        print("Robot urobil krok v pred")        
        self.ukony_do_kontroly -= 1
        print(f"Ukonov do kontroly : {self.ukony_do_kontroly}")
    
    def krok_vzad(self):
        print("Robot urobil krok v zad")        
        self.ukony_do_kontroly -= 1
        print(f"Ukonov do kontroly : {self.ukony_do_kontroly}")
        

robot_1 = Robot(24,0.5)
robot_2 = Robot(22,0.7)

robot_1.krok_vpred()
robot_1.krok_vzad()

robot_1.krok_vpred()
robot_1.krok_vzad()




print(robot_1.ukony_do_kontroly)

print(robot_1.bat)
print(robot_2.del_ruk)

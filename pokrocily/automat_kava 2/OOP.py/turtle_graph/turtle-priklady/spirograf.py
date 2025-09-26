# Importy
from turtle import Turtle, Screen
import random
import turtle


# Změna barevného módu
turtle.colormode(255)


# Generování a základní nastavení objektu
# Nastavenie turtle
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(20)
turtle.colormode(255)
 
# Funkce na generování barvy
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Funkcia na obsluhu klávesy Enter
def reset():
    print("🔁 Reštartujem program...")
    spirograf()



# Vytvorenie obrazovky
screen = Screen()
screen.title("Turtle Reštart")
screen.listen()  # Aktivuje počúvanie kláves
screen.onkey(reset, "Return")  # Kláves Enter (Return)

def spirograf(gap):
    for number in range(int(360/gap)):
        tommy.pencolor(random_color())
        tommy.circle(80)
        tommy.left(gap)
        
spirograf(10)

my_screen = Screen()
my_screen.exitonclick()

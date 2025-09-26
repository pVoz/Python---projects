# Importy
from turtle import Turtle, Screen

# Generování a základní nastavení objektu
# Nastavenie turtle
arrow = Turtle()
arrow.shape("arrow")
arrow.speed(20)


screen = Screen()
screen.title("Turtle Reštart")
screen.listen()  # Aktivuje počúvanie kláves


colors = ["violet", "yellow", "pink", "black", "green", "red"]


for x in range(400):
    arrow.pencolor(colors[x%6])
    arrow.forward(x)
    arrow.left(80)

# # Modulo 
# 5 % 2 = 1
# 12 % 5 = 2

my_screen = Screen()
my_screen.exitonclick()

# TESTOVACI Súbor

from turtle import Turtle, Screen
import time


screen = Screen()
screen.bgcolor("green")
screen.title("Vitajte v Snake Games")
screen.setup(width=600, height=600)
screen.tracer(False)

square1 = Turtle("square")
square1.goto(0, 0)
square1.penup()

square2 = Turtle("square")
square2.penup()
square1.goto(-20, 0)
def move():
    for _ in range(80):
        square1.forward(-10)
        square2.forward(-10)
        time.sleep(0.1)
        screen.update()

# Funkcia na obsluhu klávesy Enter
def reset():
    print("🔁 Reštartujem program...")
    move()
    
screen = Screen()
screen.title("Turtle Reštart")
screen.listen()  # Aktivuje počúvanie kláves
move()

my_screen = Screen()
my_screen.exitonclick()

from turtle import Turtle, Screen
import random as rd
import turtle 

#zmena farb módu
turtle.colormode(255)


tommy = Turtle()

tommy.shape("turtle")
# tommy.color("red","green")
# colors = ["red","green","blue","purple", "yellow"]

def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    random_color = (r, g, b)
    return random_color
rotation = [0, 90 , 180, 270, ]
speed = 5 

for number in range(100):
    tommy.color(random_color())
    tommy.right(rd.choice(rotation))
    tommy.forward(40)
    tommy.speed(speed)
    speed += 3
    
    if number <= 10:
        tommy.pensize(number)


my_screen = Screen()

# 🔧 Prístup k tkinter oknu a jeho vysunutie do popredia
canvas = my_screen.getcanvas()
root = canvas.winfo_toplevel()

root.lift()
root.attributes('-topmost', True)
root.after(1000, lambda: root.attributes('-topmost', False))

print(tommy)
print(f"Šírka: {my_screen.window_width()}")


my_screen.exitonclick()
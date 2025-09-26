from turtle import Turtle, Screen
import random as rd
tommy = Turtle()

tommy.shape("turtle")
tommy.color("red","green")
tommy.pensize(2)
colors = ["red","green","blue","purple"]



my_screen = Screen()


moves = int(2)  

while moves != 9:
    random_color = rd.choice(colors)
    tommy.pencolor(random_color)
    for _ in range(moves):
        tommy.forward(100)
        tommy.right(360/moves)
    moves += 1






# 🔧 Prístup k tkinter oknu a jeho vysunutie do popredia
canvas = my_screen.getcanvas()
root = canvas.winfo_toplevel()

root.lift()
root.attributes('-topmost', True)
root.after(1000, lambda: root.attributes('-topmost', False))

print(tommy)
print(f"Šírka: {my_screen.window_width()}")


my_screen.exitonclick()
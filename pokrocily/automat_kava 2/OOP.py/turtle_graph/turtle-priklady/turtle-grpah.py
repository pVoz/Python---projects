from turtle import Turtle, Screen

tommy = Turtle()

tommy.shape("turtle")
tommy.color("red","green")

for key in range(10):
    tommy.pendown()
    tommy.forward(20)
    tommy.penup()
    tommy.forward(20)






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

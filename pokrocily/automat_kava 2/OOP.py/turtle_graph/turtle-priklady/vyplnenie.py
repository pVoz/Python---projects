from turtle import Turtle, Screen


arrow1 = Turtle("arrow")
arrow2 = Turtle("arrow")
arrow1.color("red")
arrow2.color("green")
arrow1.pensize(2)
arrow2.pensize(2)
arrow1.circle(20)


for i in range(30, 100, 10):
    arrow2.circle(i)


screen = Screen()
screen.exitonclick()

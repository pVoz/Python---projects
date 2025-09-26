from turtle import Turtle, Screen
import time
import random as rd

# premenne ( atributy )
score = 0
highest_score = 0



screen = Screen()
screen.bgcolor("green")
screen.title("Vitajte v Snake Games")
screen.setup(width=600, height=600)
screen.tracer(False)

my_screen = Screen()
# screen.tracer(False)

# Hadia Hlava - Jablko - Score
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)

# Jablko
apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100,100)


# Score
score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write(f"Skóre: {score} Najvyšší skóre: 0" , align="center", font=("Arial", 18))
# časti ktoré sa pridávajú za hlavu
body_parts = []

# funkcie
head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def move_up():
     
    if head.direction != "down":
        head.direction = "up"
        
def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_left():
    if head.direction != "right":
        head.direction = "left"

# # Funkcia na obsluhu klávesy Enter
# def reset():
#     print("🔁 Reštartujem program...")

screen.listen()  # Aktivuje počúvanie kláves
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")


# Hlavný cyklus
while True:
    screen.update()       
    

    # Kontrola nabúrania s okrajmi 
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290 :
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"
        
    # Skryjeme jednotlivé časti tela
        for one_body_part in body_parts:
            one_body_part.goto(1500, 1500)
        
        # Vyprazdnime list s častami tela (sivé štvorce)
        body_parts.clear()  
          
        # resetovanie skóre
        score = 0
   
        score_sign.clear()
        score_sign.write(f"Skóre: {score} Najvyšší skóre: {highest_score}" , align="center", font=("Arial", 18))
   
    # Kolizia hlavy s jablkom - had zje jablko    
    if head.distance(apple) < 20:
        x = rd.randint(-280, 280)
        y = rd.randint(-280, 280)
        apple.teleport(x, y)
    
        #pridanie časti tela
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)
        
        # Zvýšenie scóre
        score += 10
        
        if score > highest_score:
            highest_score = score
            
            # vypisanie nového skóre
        score_sign.clear()
        score_sign.write(f"Skóre: {score} Najvyšší skóre: {highest_score}" , align="center", font=("Arial", 18))
   
    for index in range(len(body_parts) -1, 0, -1):
        x = body_parts[index -1].xcor()
        y = body_parts[index -1].ycor()
        body_parts[index].goto(x, y)
        
        
    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)
    
    move() 
    
    # Hlava narazila do tela 
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"
            

            # Skryjeme jednotlivé časti tela
            for one_body_part in body_parts:
                one_body_part.goto(1500, 1500)
                
            #Vypraznovanie listu časti tela (sivé)
            body_parts.clear()
            
            # resetovanie skóre
            score = 0
    
            score_sign.clear()
            score_sign.write(f"Skóre: {score} Najvyšší skóre: {highest_score}" , align="center", font=("Arial", 18))
    
            
    time.sleep(0.1)




my_screen.exitonclick()

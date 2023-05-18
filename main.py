import turtle
import random

snake = []

def partcreation():
    snakepart = turtle.Turtle()
    snakepart.speed(0)
    snakepart.color("white")
    snakepart.shape("square")
    snakepart.penup()
    if len(snake) == 0:
        snakepart.goto(0, 0)
    else:
        snakepart.goto(snake[-1].xcor(), snake[-1].ycor())
    snake.append(snakepart)

def right():
    if snake[0].heading() != 180:
        snake[0].setheading(0)

def left():
    if snake[0].heading() != 0:
        snake[0].setheading(180)

def up():
    if snake[0].heading() != 270:
        snake[0].setheading(90)

def down():
    if snake[0].heading() != 90:
        snake[0].setheading(270)

def createfruit():
    fruit = turtle.Turtle()
    fruit.color("red")
    fruit.shape("circle")
    fruit.penup()
    fruit.goto(random.randint(-150,150), random.randint(-150,150))
    return fruit

def movesnake():
    for i in range(len(snake)-1, 0, -1):
        snake[i].goto(snake[i-1].xcor(), snake[i-1].ycor())
    snake[0].forward(20)

def eatfruit(fruit):
    fruit.goto(random.randint(-150, 150), random.randint(-150, 150))
    partcreation()

my_screen = turtle.Screen()
my_screen.setup(width=350,height=350)
my_screen.bgcolor("black")
my_screen.title("snake game")

partcreation()

my_screen.listen()
my_screen.onkey(right, "d")
my_screen.onkey(left, "q")
my_screen.onkey(up, "z")
my_screen.onkey(down, "s")

fruit = createfruit()

while True:
    my_screen.update()
    if snake[0].distance(fruit)<20:
        eatfruit(fruit)
    movesnake()
    if snake[0].xcor()>170 or snake[0].xcor()<-170 or snake[0].ycor()>170 or snake[0].ycor()<-170:
        break
    for part in snake[1:]:
        if snake[0].distance(part) < 20:
            break
    turtle.sleep(0.1)

my_screen.exitonclick()

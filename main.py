import turtle
import random

snake = []

def partcreation():
    snakepart = turtle.Turtle()
    snakepart.speed(1)
    snakepart.color("white")
    snakepart.shape("square")
    snakepart.penup()
    if len(snake) == 0:
        snakepart.goto(0, 0)
    else:
        snakepart.goto(snake[-1].xcor(), snake[-1].ycor())
    for snakepart in snake:
        snakepart.speed(len(snake))
    snake.append(snakepart)

def right():

        snake[0].setheading(snake[0].heading() - 90)

def left():

        snake[0].setheading(snake[0].heading() + 90)



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

def snakecolision(snake):
    for snakepart in snake[1:]:
        if snake[0].distance(snakepart) < 10:
            return True

my_screen = turtle.Screen()
my_screen.setup(width=350,height=350)
my_screen.bgcolor("black")
my_screen.title("snake game")

partcreation()


my_screen.listen()
my_screen.onkey(right, "d")
my_screen.onkey(left, "q")

fruit = createfruit()

while True:

    if snake[0].distance(fruit)<20:
        eatfruit(fruit)
    movesnake()
    if snakecolision(snake):
        break
    if snake[0].xcor()>170 or snake[0].xcor()<-170 or snake[0].ycor()>170 or snake[0].ycor()<-170:
        break
    for part in snake[1:]:
        if snake[0].distance(part) < 20:
            break
    

my_screen.exitonclick()

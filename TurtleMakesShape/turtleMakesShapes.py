from turtle import Turtle, Screen
import random
turtle = Turtle()

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'aqua']

for i in range(3,5):
    random.shuffle(colors)
    for _ in range(i):
        turtle.pencolor(colors[0])
        turtle.forward(100)
        angle = 360 / i
        turtle.right(angle)

ws = Screen()
ws.exitonclick()
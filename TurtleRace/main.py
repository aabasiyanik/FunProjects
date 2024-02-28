from turtle import Turtle, Screen
import random

turtles = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)

isValid = False
while not isValid:
    user_bet = screen.textinput("Make your bet", "Which turtle will win? Enter a color: ")
    if user_bet in turtles:
        isValid = True
    else:
        print(f"Invalid color. Please enter a valid color: {turtles}")

made_turtles = []
for turtle in turtles:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + turtles.index(turtle) * 40)
    made_turtles.append(new_turtle)

isRaceOn = True
while isRaceOn:
    for turtle in made_turtles:
        if turtle.xcor() > 230:
            isRaceOn = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                break
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                break
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()
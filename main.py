# A basic turtle racing/betting game

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
player_bet = screen.textinput(title="Betting Screen", prompt="Enter the color of a turtle you bet in lower case: ")

turtles = []
colors = ("red", "orange", "yellow", "green", "blue", "purple")
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + i * 40)
    turtles.append(new_turtle)

is_race_on = True
while is_race_on:

    for i in turtles:
        rand = random.randint(1, 10)
        i.forward(rand)
        if i.xcor() > 230:
            is_race_on = False
            turtle_won = i
            if player_bet == turtle_won.pencolor():
                print(f"You won! The turtle won the race is indeed {turtle_won.pencolor()}")
            else:
                print(f"You lost! The turtle won the race is {turtle_won.pencolor()}")

screen.exitonclick()

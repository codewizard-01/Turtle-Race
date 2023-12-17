from turtle import Turtle
from turtle import Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color: ")
colors = ["red", "orange", "blue", "yellow", "purple", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for index in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    new_turtle.color(colors[index])
    all_turtles.append(new_turtle)

is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You have won. The {winning_color} is the winner.")
            else:
                print(f"You have lost. The {winning_color} is the winner.")

        distance = random.randint(0, 10)
        turtle.forward(distance)





screen.exitonclick()


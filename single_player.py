from turtle import Turtle
from turtle import Screen
import random


class SinglePlayer:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=500, height=400)
        self.user_bet = self.screen.textinput(title="Make your bet",
                                              prompt="Which turtle will win the race? Choose a color: ")
        self.colors = ["red", "orange", "blue", "yellow", "purple", "green"]
        self.y_positions = [-70, -40, -10, 20, 50, 80]
        self.all_turtles = []
        self.create_turtle()
        self.who_wins()

    def create_turtle(self):
        for index in range(6):
            new_turtle = Turtle()
            new_turtle.shape("turtle")
            new_turtle.penup()
            new_turtle.goto(x=-230, y=self.y_positions[index])
            new_turtle.color(self.colors[index])
            self.all_turtles.append(new_turtle)

    def who_wins(self):
        is_game_on = True
        while is_game_on:
            for turtle in self.all_turtles:
                if turtle.xcor() > 230:
                    is_game_on = False
                    winning_color = turtle.pencolor()
                    if self.user_bet == winning_color:
                        print(f"You have won. The {winning_color} is the winner.")
                    else:
                        print(f"You have lost. The {winning_color} is the winner.")

                distance = random.randint(0, 10)
                turtle.forward(distance)

        self.screen.exitonclick()


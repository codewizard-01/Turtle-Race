from turtle import Turtle
from turtle import Screen
import random


class Multiplayer:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=500, height=400)
        self.participant_num = self.screen.textinput(title="Let's bet",
                                                     prompt="How many people want to bet? Enter the number!")
        self.user_bets = []
        for i in range(int(self.participant_num)):
            self.user_bet = self.screen.textinput(title="Make your bet",
                                                  prompt=f"{i + 1}:Which turtle will win the race? Choose a color:")
            self.user_bets.append(self.user_bet)
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
        winners = []
        losers = []
        while is_game_on:
            for turtle in self.all_turtles:
                if turtle.xcor() > 230:
                    is_game_on = False
                    winning_color = turtle.pencolor()
                    for index, bet in enumerate(self.user_bets):
                        if bet == winning_color:
                            print(f"{index + 1} has won.")
                            winners.append(index + 1)
                        else:
                            print(f"{index + 1} have lost.")
                            losers.append(index + 1)
                    print(f"The {winning_color} is the winner.")

                distance = random.randint(0, 10)
                turtle.forward(distance)

        self.screen.exitonclick()


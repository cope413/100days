from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('chartreuse')
        self.hideturtle()
        self.score = 0
        self.goto(0, 275)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, 'normal'))

    def point(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, 'normal'))

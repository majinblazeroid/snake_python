from turtle import Turtle,colormode
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        with open('highscore_text.txt', mode='r') as file:
            hs = (file.read())
        super().__init__()
        self.score = 0
        self.high_score = int(hs)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} Highscore: {self.high_score}",font=("Arial",18,"normal"),align="center")
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}",font=("Arial",18,"normal"),align="center")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('highscore_text.txt', mode='w') as file:
            file.write(f'{self.high_score}')
        self.score = 0
        self.increase_score()
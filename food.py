from turtle import Turtle, colormode
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.x = random.randint(-280,280)
        self.y = random.randint(-280, 280)
        self.goto(self.x,self.y)

    def refresh(self):
        self.x = random.randint(-280,280)
        self.y = random.randint(-280, 280)
        self.goto(self.x,self.y)


from turtle import Turtle as t, colormode
import random
MOVE_DIST = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
colormode(255)

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.move_speed = 0.1

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_snake = t(shape='square')
        new_snake.color('white')
        new_snake.penup()
        if position is not (0,0):
            new_snake.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        new_snake.goto(position)
        self.snake.append(new_snake)

    def reset(self):
        for snake in self.snake:
            snake.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for j in range(len(self.snake) - 1, 0, -1):
            self.snake[j].goto(self.snake[j - 1].pos())  # moves the snake in reverse
        self.snake[0].forward(MOVE_DIST)  # moves the first segment forward

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)



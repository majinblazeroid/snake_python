from turtle import Screen
import time
import math
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('KYA BE SAALE GAME KHELEGA?')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

cont = True
while cont:
    screen.update()
    time.sleep(snake.move_speed)
    snake.move()

    #for when the snake catches food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        snake.move_speed *= 0.999

    #detect collision
    if math.fabs(snake.head.xcor()) > 295 or math.fabs(snake.head.ycor()) > 295:
        scoreboard.reset()
        snake.reset()
        #cont = False
        #scoreboard.over()

    for segment in snake.snake:
        if segment != snake.head:
            if snake.head.distance(segment) <10:
                scoreboard.reset()
                snake.reset()
                #cont = False
                #scoreboard.over()


screen.exitonclick()

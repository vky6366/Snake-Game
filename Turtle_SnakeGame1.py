from turtle import Turtle, Screen
import random
import time
from Turtle_SnakeGame2 import Snake
from Turtle_SnakeGame3 import Food
from Turtle_SnakeGame4 import S_Board

# this is called comment

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
scores = S_Board()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    #seg[0].left(90)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scores.increase_score()

    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor() < -280:
        snake.reset()
        scores.reset_score()

    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 10:
            snake.reset()
            scores.reset_score()

screen.exitonclick()

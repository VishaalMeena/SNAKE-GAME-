from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import turtle

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#draw boundary
# Draw boundary
border = turtle.Turtle()
border.hideturtle()
border.color("green")
border.pensize(3)
border.penup()
border.goto(-280, 250)   # starting point (top-left corner)
border.pendown()

for _ in range(4):  # draw square
    border.forward(560)   # each side length
    border.right(90)


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    #detecting collision b/w food and snake
    if snake.head.distance(food) <= 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    #detecting if snake has hit the wall or not
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 250 or snake.head.ycor() < -310):
        is_game_on = False
        scoreboard.game_over()

    snake.move()

    # Detect collision on tail
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on == False
            scoreboard.game_over()


screen.exitonclick()
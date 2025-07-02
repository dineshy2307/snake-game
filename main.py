from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.15)
    snake.move()
    if not snake.check():
        score.game_over()
        game_over = True
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.grow()
        score.up_score()
        score.put_score()
    for tail in snake.turtles[1:]:
        if snake.turtles[0].distance(tail) < 10:
            score.game_over()
            game_over = True


screen.exitonclick()

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.tracer(n=0)
my_screen.title('Snake Game')
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')

scoreboard = ScoreBoard()
snake = Snake()
food = Food()

my_screen.update()
my_screen.listen()
my_screen.onkey(fun=snake.up, key='Up')
my_screen.onkey(fun=snake.down, key='Down')
my_screen.onkey(fun=snake.left, key='Left')
my_screen.onkey(fun=snake.right, key='Right')

game_is_on = True

while game_is_on:
    snake.move()
    my_screen.update()
    time.sleep(0.1)

    # food eating
    if snake.snake_head.distance(food) < 15:
        food.refresh_food()
        scoreboard.update_score()
        snake.extend_a_segment()

    # wall collision
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or\
            snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_is_on = False

    # tail collision
    for segment in snake.list_of_snake_segments[1::]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False


scoreboard.game_over()
my_screen.exitonclick()

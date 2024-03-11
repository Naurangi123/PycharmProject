from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def restart_game():
    snake.reset_snake()
    food.refresh()
    scoreboard.reset_game()

# Function to handle click events for the restart button
def on_restart_click(x, y):
    if -50 < x < 50 and -50 < y < 50:
        restart_game()

def game_loop():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()

        if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
            scoreboard.game_over()
            screen.update()
            restart_game()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                screen.update()
                restart_game()

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initialize snake, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keyboard inputs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Create a restart button
restart_button = Turtle()
restart_button.shape("square")
restart_button.color("white")
restart_button.shapesize(stretch_wid=1, stretch_len=4)
restart_button.penup()
restart_button.goto(0, -280)
restart_button.write("Restart", align="center", font=("Courier", 16, "normal"))
restart_button.onclick(on_restart_click)

game_is_on = True
game_loop()

screen.exitonclick()

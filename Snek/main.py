from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)
mode = screen.textinput("Choose Difficulty Level", "Easy, Normal, or Hard")

if mode == 'easy':
    difficulty = 0.25
elif mode == 'normal':
    difficulty = 0.1
elif mode == 'hard':
    difficulty = 0.05
else:
    difficulty = 0.1


def snek():
    snake = Snake()
    food = Food()
    score = Scoreboard()
    game_is_on = True

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while game_is_on:
        screen.update()
        time.sleep(difficulty)
        snake.move()

        # Collision detection with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.point()

        # Collision detection with walls
        if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
            score.game_over()
            again = screen.textinput("Game Over", "Try Again? Y or N").lower()
            if again == 'y':
                screen.reset()
                snek()
                game_is_on = True
            else:
                game_is_on = False
                screen.exitonclick()

        # Collision detection with self
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.game_over()
                again = screen.textinput("Game Over", "Try Again? Y or N").lower()
                if again == 'y':
                    screen.reset()
                    snek()
                    game_is_on = True
                else:
                    game_is_on = False
                    screen.exitonclick()


snek()
screen.exitonclick()

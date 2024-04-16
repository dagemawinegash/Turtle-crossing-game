import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
scoreboard = Scoreboard()

turtle = Player()

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.make_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if turtle.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    # if reached top
    if turtle.ycor() > 280:
        turtle.reset_position()
        car_manager.speed_up()
        scoreboard.level_up()

screen.exitonclick()

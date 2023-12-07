import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#keystroke vandeling
screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(car_manager.game_speed)
    screen.update()
    car_manager.creat_car()
    
    
    for car in car_manager.cars:
        car.car_move()    # Move each car
        
        if player.distance(car) < 25 and car.xcor() <= 0:     #detect when the turtle player collides with a car
            scoreboard.game_over()
            game_is_on = False   

        if player.ycor() > Player.FINISH_LINE_Y:
            player.setposition(Player.STARTING_POSITION)
            scoreboard.increase_score()
            car_manager.level_up()







screen.exitonclick()

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5



class CarManager(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.x_move = 10
        self.y_move = 10
        self.goto(250, random.randint(-250, 250)) 
        self.cars = []
        self.count = 0
        self.move_increcment = 5
        self.game_speed = (1 / self.move_increcment)
    
    def car_move(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, self.ycor())
    
    def creat_car(self):
        '''Creates cars that are randomly generated along the y-axis and move to the left edge of the screen'''
        if self.count % 6 == 0:   #generate a new car only every 6th time the game loop runs
            new_car = CarManager()
            self.cars.append(new_car)
            new_car.position()    
        self.count += 1
    
    def level_up(self):
        '''return the turtle to the starting position and increase the speed of the cars'''
        self.move_increcment *= 2
        self.game_speed = 1 / self.move_increcment

        
             



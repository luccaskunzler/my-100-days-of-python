from turtle import Turtle
import random

# list of possible colors for the cars
COLORS = ['black', 'red', 'purple', 'red', 'blue', 'yellow', 'orange', 'pink']
# lines or streets in which the cars will drive
LINES = [-180, -140, -100, -60, -20, 20, 60, 100, 140]


class Car(Turtle):
    def __init__(self, index, multiplier):
        super().__init__()
        self.penup()
        # accordingly with the index, the car is placed in a different line/street 
        self.goto(300, LINES[index])
        # defines the square shape and modify it to a rectangle of 1x2 pixels
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        # select random color to car
        self.color(random.choice(COLORS))
        # self.SPEEDS = [5, 10, 20, 5, 10, 20, 5, 10, 20]
        # list of speeds - each line/street will have its own speed
        self.SPEEDS = [1, 2, 4, 1, 2, 4, 1, 2, 4]
        self.own_index = index
        # multiplier is used to speed up the cars...
        # if the player continues alive in the game
        self.faster = multiplier

    def move(self):
        self.forward((self.SPEEDS[self.own_index])*self.faster)
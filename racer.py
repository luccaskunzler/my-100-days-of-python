# this file creates the player or racer
import time
from turtle import Turtle
import random
# constant to determine how much the player should move at each keypress 
# 40 means crossing a complete 'street' from the middle point to middle point
STEPS = 40


class Racer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.origin()
        self.shape('turtle')
        self.color('red')
        self.setheading(90)

    # the following functions control the moves of the player
    # go_forward could also be used as go_up
    def go_forward(self):
        self.forward(STEPS)

     # go_backward could also be used as go_down
    def go_backwards(self):
        self.backward(STEPS)

    # for lateral move, half of the step is used...
    #  to increase the mobility of the player
    def go_right(self):
        new_x = self.xcor() + STEPS/2
        self.setposition(x=new_x, y=self.ycor())

    def go_left(self):
        new_x = self.xcor() - STEPS/2
        self.setposition(x=new_x, y=self.ycor())

    # places the player at the origin
    def origin(self):
        self.setposition(0, -260)

import time
from turtle import Turtle
import random
STEPS = 40


class Racer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.origin()
        self.shape('turtle')
        self.color('red')
        self.setheading(90)

    def go_forward(self):
        self.forward(STEPS)

    def go_backwards(self):
        self.backward(STEPS)

    def go_right(self):
        new_x = self.xcor() + STEPS/2
        self.setposition(x=new_x, y=self.ycor())

    def go_left(self):
        new_x = self.xcor() - STEPS/2
        self.setposition(x=new_x, y=self.ycor())

    def origin(self):
        self.setposition(0, -260)

# creates the dashed lines to separate the streets
from turtle import Turtle
HEIGHTS = [-200, -160, -120, -80, -40, 0, 40, 80, 120, 160]

class Lines(Turtle):
    def __init__(self,index):
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(-300, HEIGHTS[index])
        self.setheading(0)
        self.pendown()
        self.hideturtle()
        self.width(1)
        while self.xcor() < 280:
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()

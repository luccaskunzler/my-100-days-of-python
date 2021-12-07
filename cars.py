from turtle import Turtle
import random
COLORS = ['black', 'red', 'purple', 'red', 'blue', 'yellow', 'orange', 'pink']
LINES = [-180, -140, -100, -60, -20, 20, 60, 100, 140]


class Car(Turtle):
    def __init__(self, index, multiplier):
        super().__init__()
        self.penup()
        self.goto(300, LINES[index])
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.color(random.choice(COLORS))
        # self.SPEEDS = [5, 10, 20, 5, 10, 20, 5, 10, 20]
        self.SPEEDS = [1, 2, 4, 1, 2, 4, 1, 2, 4]
        self.own_index = index
        self.faster = multiplier

    def move(self):
        self.forward((self.SPEEDS[self.own_index])*self.faster)
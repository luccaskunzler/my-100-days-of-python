from turtle import Turtle
import time
CONFIG = ('Courier', 16, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.goto(0,270)
        self.print_score()

    def print_score(self):
        self.write(f"Score is {self.score}", align='center', font=CONFIG)

    def update_score(self):
        self.clear()
        self.score += 1
        self.print_score()

    def game_over(self):
        self.clear()
        self.write("GAME OVER", align='center', font=CONFIG)
        time.sleep(2)
        self.clear()
        self.score = 0
        self.print_score()

    def good_bye(self):
        self.goto(0, 0)
        self.write("GOOD BYE", align='center', font=('Courier', 40, 'normal'))
        self.goto(0, -50)
        self.write("Click in the screen to exit", align='center', font=('Courier', 20, 'normal'))


class Exit(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(-250, -250)
        self.print_exit()

    def print_exit(self):
        self.write(f"← Exit ", align='center', font=CONFIG)
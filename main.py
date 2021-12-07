'''
Game of turtle crossing the road, the 23rd day challenge of 100 days of Python
06/Dec/2021 17:06
'''

import time
from turtle import Screen
from lines import Lines
from racer import Racer
from cars import Car
import random
from score import Score, Exit

# initiates the screen objects
screen = Screen()
# sets size and color
screen.setup(width=600, height=600)
screen.bgcolor('grey')
# disables the tracer to improve the animation
screen.tracer(0)
# enables the .listen cmd to listen once a key is pressed
screen.listen()


racer = Racer()
score = Score()
exit = Exit()

playing = True
while playing:

    # creates the center line or net
    list_of_lines = []
    for i in range(0, 10):
        list_of_lines.append(Lines(i))

    # creates the list of car objects
    cars = []

    # sets the initial conditions for the 'alive' loop to iterate
    # will be used to create a new car only when the number is a multiple of a chosen constant
    counter = 0
    # sets the score to zero
    score.score = 0
    # sets the multiplier for the speed of the cars - initial state unity
    faster = 1
    alive = True

    while alive:
        # for every 10 loops, a new car is created. This parameter was hand tuned in a try and error method
        if counter % 10 == 0:
            cars.append(Car(index=(random.randint(0, 8)), multiplier=faster))

        # sets the functions to each one of the possible key to be pressed (arrows)
        screen.onkey(key='Up', fun=racer.go_forward)
        screen.onkey(key='Down', fun=racer.go_backwards)
        screen.onkey(key='Left', fun=racer.go_left)
        screen.onkey(key='Right', fun=racer.go_right)

        # increases the counter
        counter += 1

        # sets conditions if turtle reached the other side of the road
        if racer.ycor() >= 180:
            screen.update()
            # a point is added
            score.update_score()
            time.sleep(2)
            # as the screen text is cleared in the update score, another indication for the exit is necessary
            exit.print_exit()
            # puts the turtle back in the origin
            racer.origin()
            # increases the speed for next round
            faster *= 1.1

        # sets the condition is user want to exit
        if racer.xcor() < -280 and racer.ycor() < -210:
            # finished both loops
            alive = False
            playing = False
            time.sleep(1)
            # cleans the screen, sets it to a black color so the good bye message can be printed
            screen.clear()
            screen.bgcolor('black')
            score.good_bye()

        # block that deals with all the cars move and collisions
        for car in cars:
            # moves all the existing cars in the list
            car.move()
            # if any car is at a closer distance than 20, game over
            if car.distance(racer) < 20:
                alive = False
                # activates game_over routine
                score.game_over()
                # puts turtle back to origin
                racer.origin()
                # with Turtle, I couldn't find a way to delete the objects, so I am reseting them and moving them away
                for car in cars:
                    car.reset()
                    car.penup()
                    car.goto(400,400)
                    car.hideturtle()

        # updates the screen, given the selected sleep time - try and error here as well
        time.sleep(0.01)
        screen.update()


# exits on click
screen.exitonclick()
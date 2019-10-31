# Thomas Marshall
# bumperCars.py
#   This program will randomly generate a direction and speed of two balls
#   that bounce of of the walls and walls and change their color on impact.
# I certify this lab is my own work, but I discussed it with Nick Mancabelli.

# Imports needed for graphics, math, random, and time.
from graphics import *
import random
from math import *
import time

# Main function that runs the full program
def bumper():
    # Build window    
    width = 500
    height = 500
    win = GraphWin("Bumper Cars", width, height)
    win.setBackground(randomColor())

    # First ball
    pt = Point(100, 240)
    ball = Circle(pt, 50)
    ball.setFill(randomColor())
    ball.setWidth(5)
    ball.draw(win)

    # Second ball
    pt2 = Point(400, 300)
    ball2 = Circle(pt2, 50)
    ball2.setFill(randomColor())
    ball2.setWidth(5)
    ball2.draw(win)

    # Random direction generator
    ballxD = getRandom(15)
    ballyD = getRandom(15)
    ball2xD = getRandom(15)
    ball2yD = getRandom(15)

    # Range to keep the balls moving
    while 3 < 5:
        # Time staller
        time.sleep(.015)
        # Balls continue to move
        ball.move(ballxD, ballyD)
        ball2.move(ball2xD, ball2yD)

        # Ball collision code
        if didCollide(ball, ball2):
            ballxD = ballxD * -1
            ballyD = ballyD * -1
            ball.setFill(randomColor())
            ball2xD = ball2xD * -1
            ball2yD = ball2yD * -1
            ball2.setFill(randomColor())

        # Side collision code
        if hitHorizontal(ball) == True:
            ballxD = ballxD * -1
        if hitVertical(ball) == True:
            ballyD = ballyD * -1

        # Top and bottom collision code
        if hitHorizontal(ball2) == True:
            ball2xD = ball2xD * -1
        if hitVertical(ball2) == True:
            ball2yD = ball2yD * -1

    # Close window message
    message = Text(Point(width/2, height - 30), "Click to close.")
    message.draw(win)
    # Closes window
    win.getMouse()
    win.close()

# Function to find a random output
def getRandom(moveAmount):
    # Range of random numbers
    beginning = moveAmount * -1
    end = moveAmount
    # Returns the randomized outputs
    return random.randrange(beginning, end)

# Function to determine if the balls connect
def didCollide(ball, ball2):
    # Failsafe for when the balls do not connect
    collide = False

    # First ball data grab
    ballR = ball.getRadius()
    ballC = ball.getCenter()
    ballx = ballC.getX()
    bally = ballC.getY()

    # Second ball data grab
    ball2R = ball2.getRadius()
    ball2C = ball2.getCenter()
    ball2x = ball2C.getX()
    ball2y = ball2C.getY()

    # Calculates distance between the two circles' centers
    hit = sqrt((ball2x - ballx) ** 2 + (ball2y - bally) ** 2)

    # If statement to determine if the distance between centers is greater than the sum
    # of the radii
    if hit <= 100:
        collide = True
    # Returns answer
    return collide

# Function to determine if a ball hits a side
def hitHorizontal(ball):
    # Failsafe
    hit = False
    # Find the designated ball's center
    ball = ball.getCenter().getX()

    # Determines if the center is closer to the side than the radius is long
    if ball <= 50 or ball >= 450:
        hit = True
    # Returns answer
    return hit

# Function to determine if a ball hits the top or bottom
def hitVertical(ball):
    # Failsafe
    hit = False
    # Find the designated ball's center
    ball = ball.getCenter().getY()

    # Determines if the center is closer to the top or bottom than the radius is long
    if ball <= 50 or ball >= 450:
        hit = True
    # Returns answer
    return hit

# Function to randomize color
def randomColor():
    # Randomize each color in rgb
    red = random.randrange(255)
    blue = random.randrange(255)
    green = random.randrange(255)
    # Random selections entered into color code
    color = color_rgb(red, blue, green)
    # Returns what color was randomly selected
    return color


# Auto runs the main function
bumper()

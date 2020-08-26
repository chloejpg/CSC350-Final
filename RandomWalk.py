"""
Chloe Brown
Random Walk
This program has a turtle walk inside a circle with radius 100 units
until the turtle has left the perimeter. The program also counts
how many steps it takes the turtle to leave the circle.
"""

import turtle
from random import randrange
from math import *

#gives turtle the shape
#creates set variable for radius
turtle.shape("turtle")
RADIUS = 100

def set_up_program():
     #this function draws the "red" circle boundary
     #sets pen color to "black"
     #sets starting position to the origin
     turtle.penup()
     turtle.setposition(0,-100)
     turtle.pendown()
     turtle.color("red")
     turtle.circle(RADIUS)
     turtle.color("black")
     turtle.penup()
     turtle.setposition(0,0)
     turtle.pendown()

def random_walk(step_size, max_turn):
     #the function is defined in terms of number of units forward
     #and the maximum degrees for a turn to the left.
     #the count is set to 0 initially.
     count = 0
     while turtle.distance(0,0) < RADIUS:
          #while the turtle's distance from the origin is
          #less than 100 (radius) units,
          #the turtle moves forward and turns left.
          #the count increases by 1.
          count += 1
          turtle.forward(step_size)
          turn = randrange(0, max_turn, 45)
          turtle.left(turn)
     while turtle.distance(0,0) >= RADIUS:
          #while the turtle's distance from the origin is
          #greater than 100 (radius) units,
          #the turtle has exited the circle and stops moving
          return count

#the program begins and runs with step size 10 and maximum degrees 315
set_up_program()  
random_walk(10, 315)

#total number of steps taken is printed after the turtle exits the circle's perimeter
print("Total steps: ",count)



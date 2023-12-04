# Functions and Turtle
# Damien Cheng
# Nov 28

import turtle

marine = turtle.Turtle()
marine.color("red")
marine.shape("circle") 

def square(sidelength: float) -> float:
	
	area = sidelength ** 2
	return area

def squared(num: float) -> float:
    """Returns the given number squared"""
    return num**2


def draw_square(side_length: float) -> None:
    for _ in range(4):
        marine.forward(side_length)
        marine.left(90)


marine.speed(0)

# Create a squares that get bigger and bigger
for i in range(50):
    draw_square(squared(i))

turtle.done()
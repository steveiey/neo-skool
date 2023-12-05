# Functions and Turtle
# Damien Cheng
# Nov 28

import turtle

marine = turtle.Turtle()
marine.pensize(1)
marine.shapesize(.5)
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
#for i in range(50):
#    draw_square(squared(i))

def draw(level: int, length: int)-> None:
    """Draw a tree. Just cause ig.
    Params:
    level, length
     """
    marine.speed(0)
    if level > 0:
        # TRUNK
        marine.forward(length)
        # TURN (lvl-1)
        marine.left(30)
        draw(level - 1, length / 1.5)
        marine.right(60)
        draw(level-1, length/1.5)
    
        # BACK 
        marine.left(30)
        marine.back(length)
    else:
         marine.stamp()        
        # TURN
marine.seth(90)


def draw_3(level: int, length: int)-> None:
    """Draw a tree. Just cause ig.
    Params:
    level, length
     """
    marine.speed(0)
    if level > 0:
        # TRUNK
        marine.forward(length)
        # TURN (lvl-1)
        marine.left(30)
        draw_3(level - 1, length / 1.5)
        marine.right(30)
        draw_3(level-1, length/1.5)
        marine.right(30)
        draw_3(level-1, length/1.5)
        # BACK 
        marine.left(30)
        marine.back(length)
    else:
         marine.stamp()        
        # TURN
marine.seth(90)
draw_3(4,150)

turtle.done()
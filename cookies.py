
# Cookies
# Author: Damien Cheng
# 21 November 2023

import turtle
#cookie one
# Make baker turtle
baker_turtle = turtle.Turtle()
turtle.speed(0)
def make_cookie(x: int, y: int):
    """Draws a cookie on the screen at (x, y)
    
    Params:
    x - x-coordinate of the centre of cookie
    y - y-coordinate of the centre of cookie"""
   
   
    baker_turtle.color("brown")
    baker_turtle.penup()
    baker_turtle.goto(-5+x, -30+y)
    baker_turtle.pendown()
    baker_turtle.circle(30)
    baker_turtle.penup()

    baker_turtle.color("black")
    baker_turtle.goto(0+x,0+y)
    baker_turtle.stamp()
    baker_turtle.goto(10+x, 10+y)
    baker_turtle.stamp()
    baker_turtle.goto(10+x, -10+y)
    baker_turtle.stamp()
    baker_turtle.goto(-10+x,10+y)
    baker_turtle.stamp()
    baker_turtle.goto(-10+x, -10+y)
    baker_turtle.stamp()

for i in range(1000):
    make_cookie(i, i)
  
turtle.done()
#pumpkin drawing
#damien cheng
# sus


import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()


# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Nose
carver.penup()
carver.setposition(0, 0)
carver.dot(10)
carver.forward(15)

# eye line
carver.setpos(-50, 30)
carver.pensize(40)
carver.pendown()
carver.forward(100)

# eye
carver.setpos(-30, 30)
carver.color("white")
carver.pensize(10)
carver.forward(.1)
carver.penup()

carver.setpos(30, 30)
carver.pendown()
carver.backward(.1)
carver.penup()
carver.forward(500)

#mouth







turtle.done()
#Turtle Example
#Damien Cheng
# Nov 21
import turtle
#create turtle
steve = turtle.Turtle()
#do things from user
#Constants
TURTLE_MAGTITUDE = 20




print("""To give commands, type:
w to go up
a to go left
s to go down
d to go right
done to be done""")


done = False

while not done:
    command = input("where should I go?")
    if command.lower().strip(" ..?!") == "w":
        steve.forward(TURTLE_MAGTITUDE)
    
    elif command.lower().strip(" ..?!") == "a":
        steve.left(45)
    
    elif command.lower().strip(" ..?!") == "s":
        steve.back(TURTLE_MAGTITUDE)
    
    elif command.lower().strip(" ..?!") == "d":
        steve.right(45)
    
    elif command.lower().strip(" .,?!") == "done":
        done = True



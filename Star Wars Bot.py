# Star Wars Bot
# Damien Cheng
# Oct 16

# DECIDE IF LIGHT or DARKKKKKKK
print("I will decide if you can join the Dark Side.")
print("IS...")
colour = input("RED... your favourite colour!?")

if colour.strip(" ,.?!").lower() == "yes":
    print("Welcome to the dark side... I GUESS.")
else:
    print("Not over yet but it is not looking good...")
    capes = input("Are you an avid fan of capes perchance?")
    if capes.strip(" ,.?!").lower() == "yes":
        print("yeah. WELCOME TO")
        print("THE DARK SIDE")
    else:
        print("go away...")
        print("jedi...")





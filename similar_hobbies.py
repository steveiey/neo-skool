#similar hobbies
# Damien Cheng
# Nov 14

simscore = 0
likes_1 = input("Tell me what you like. seperate them by spaces. they gotta be one word each").lower().split(" ")

likes_2 = input("Tell me what you like. seperate them by spaces. they gotta be one word each").lower().split(" ")

for like in likes_1:
        if like in likes_2:
                simscore += 1

print(f"Person 1:{likes_1}")
print(f"Person 2:{likes_2}")
print(f"you have {simscore} similarities")

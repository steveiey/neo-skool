#similar hobbies
# Damien Cheng
# Nov 14

simscore = 0
likes_1 = input("Tell me what you like. seperate them by spaces. they gotta be one word each").lower()
for line in likes_1:
        p1likes = line.split(" ")

likes_2 = input("Tell me what you like. seperate them by spaces. they gotta be one word each").lower()
for line in likes_2:
        p2likes = line.split(" ")

for like in likes_1:
        if like in likes_2:
                simscore += 1

print(f"Person 1:{p1likes}")
print(f"Person 2:{p2likes}")
print(f"you have {simscore} similarities")

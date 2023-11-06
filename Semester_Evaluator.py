#Semester_Evauluator
#Damien Cheng
# Nov 3
courses = int(input("How many courses are you taking?").strip(",.?! "))
total = 0


for i in range(1, courses + 1):
    score = int(input(f"How do you rate course {i} 1 out of 5?").strip(",.?! "))
    total += score

print(score/courses)
if 1 < total > 3:
    print("Not bad")
elif 3 < total > 5:
    print("Great")
elif total < 1:
    print("ouch")
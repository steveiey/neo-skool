# parental bot
# damien Cheng
# Nov 16

questions = ["Did you eat?", "Did you study?", "Did you do your laundry?", "Did you call grandma?"]
score = 0
for question in questions:
    sus = input(question)
    if sus == "yes":
        score = score + 1


if score == 0:
    print("I'm coming over.")
elif score <= 2:
    print("Ok.")
elif score <= 4:
    print("Good!")
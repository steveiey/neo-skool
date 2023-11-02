#chip rater
#damien Cheng
#some day

#interview people about chips + rate out of 5
#tally up results

total_rating = 0


print("UWAWUAUWAWAWUAW")
print("Hi thereerererereererere")
questions = [
    "How crisp were those crispsspsppssp u 8 just now from 1 - 5. 1= bad 5= great.",
    "r8 the taste 1=blehh 5=yummm",
    "r8 the pakajing 1=disguesting 5=uyah"
]

for question in questions:
    print(question)

    r8ing = int(input().strip(",.? !"))

    total_rating = total_rating + r8ing


    avg = total_rating / len(questions)

print(f"The avg r8ing of this is {avg:.1f} /5")
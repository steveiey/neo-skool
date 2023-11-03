#olympic_judging
# Damien Cheng
# Nov 3

total_rating = 0





print("Rate the performance from 1 to 10. 10=best 1=dog poop")
r8ing_1 = int(input().strip(",.? !"))
print("Rate the performance from 1 to 10. 10=best 1=dog poop")
r8ing_2 = int(input().strip(",.? !"))
print("Rate the performance from 1 to 10. 10=best 1=dog poop")
r8ing_3 = int(input().strip(",.? !"))
print("Rate the performance from 1 to 10. 10=best 1=dog poop")
r8ing_4 = int(input().strip(",.? !"))
print("Rate the performance from 1 to 10. 10=best 1=dog poop")
r8ing_5 = int(input().strip(",.? !"))

# r8ing_1 = int(input("Rate the performance from 1 to 10. 10=best 1=dog poop"))






total_rating = total_rating + r8ing_1 + r8ing_2 + r8ing_3 + r8ing_4 + r8ing_5
avg = total_rating / 5

print(f"judge 1:{r8ing_1}")
print(f"judge 1:{r8ing_2}")
print(f"judge 1:{r8ing_3}")
print(f"judge 1:{r8ing_4}")
print(f"judge 1:{r8ing_5}")

print(f"Your Olympic score is {avg:.1f}")
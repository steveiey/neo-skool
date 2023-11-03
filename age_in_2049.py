#age_in_2049
#damien cheng
#yes

#age in 26 years

month_day = input("what da day and month? anything works").strip(",.?!")

year = int(input("what da year").strip(",.?! "))
age = int(input("What ur age?").strip(",.?! "))
year_diff = 2049 - year

age2049 = age + year_diff

print(f"Your age on {month_day} of 2049 is {age2049}")



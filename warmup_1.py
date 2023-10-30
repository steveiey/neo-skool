# Warmup
# Damien Cheng
# 9/25/23

print("BEEP BOOP")

some_string = "This is some string."
print(some_string.upper().strip(".!").lower().split())


is_raining = True
is_cloudy = True
is_sunny = True
if is_raining:
    if is_sunny:
        print("Bring your shades and your umbrella!")
    elif is_cloudy:
        print("Brrrrr.")

adjectives = ["Golden", "Tiny", "Purple"]
stars = ["Polaris", "Vega", "Sun"]
for adj in adjectives:
    for word in stars:
        print(adj + word)

for i in range(10): 
    print(i)

some_list = ["beans", "magic", "beanstalk"] 
 
print(some_list[0][1])


ubials_inventory = ["sword", "shield", "flask", "phone", "bigger sword"] 
 
if "phone" in ubials_inventory: 
    print("raining")


 
print("bigger sword" in ubials_inventory)
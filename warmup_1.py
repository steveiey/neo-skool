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
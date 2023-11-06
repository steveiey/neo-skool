# Neo world traveler bot
# Damien Cheng
# Nov 6

name = input("Wat da name be?")
print(f"Ay there {name}")

tot = 0

continents = ["Asia",
              "Europe",
              "North America",
              "South America",
              "Australia",
              "Africa",
              "Antarcica"
              ]


for continent in continents:
    sus = input(f"Have you been to {continent} (Yes/No)").lower()
    if sus == "yes":
        tot = tot + 1
print(f"Your have been to {tot}/7 continents.")
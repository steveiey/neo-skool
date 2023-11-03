#world traveler
#damien Cheng
# Nov 3

name = input("Wat da name be?")
print(f"Ay there {name}")

Asia = input("Have you been to Aisa (Yes/No)").lower()
if Asia == "yes":
    AsiaN = 1
else:
    AsiaN = 0
Euro = input("Have you been to Euro (Yes/No)").lower()
if Euro == "yes":
    EuroN = 1
else:
    EuroN = 0
NA = input("Have you been to North America (Yes/No)").lower()
if NA == "yes":
    NAN = 1
else:
    NAN = 0
SA = input("Have you been to South America (Yes/No)").lower()
if SA == "yes":
    SAN = 1
else:
    SAN = 0
Aus = input("Have you been to Australia (Yes/No)").lower()
if Aus == "yes":
    AusN = 1
else:
    AusN = 0
Africa = input("Have you been to Africa (Yes/No)").lower()
if Africa == "yes":
    AfricaN = 1
else:
    AfricaN = 0
Ant = input("Have you been to Antarctica (Yes/No)").lower()
if Ant == "yes":
    AntN = 1
else:
    AntN = 0

total = AsiaN + EuroN + NAN + SAN + AusN + AfricaN + AntN
print(f"Your have been to {total}/7 continents.")
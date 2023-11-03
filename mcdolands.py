#Mcdolands.py
#Damien Cheng
#Nov 3

# takes orde and prints out cost with tax

burger = input("Would you like a burger for $5 (Yes/No)").lower()
fries = input("Would you like fries for $3 (Yes/No)").lower()
if burger == "yes":
    burgermoney = 5
else:
    burgermoney = 0

if fries == "yes":
    friesmoney = 3
else:
    friesmoney = 0




total = (friesmoney + burgermoney) * 1.14
print(f"Your total is ${total:.2f}")
# Winter Holiday
# Jan 8 2024
# Damien Cheng
import random
positivity = input("GOOOOOOOD ORRRRRR BADDDDDDDDD").strip("!.<, ").lower()

goodlist = [
            "Worked and made money",
            "Consumed the flesh of animals",
            "isshin the sword saint first try",
            "Silver 4 in Streetfighter 6",
            "Slept",
            "Received money"
        ]
badlist = [
    "Demon of hatred is a piece of dodo",
    "Inner Genichiro is a piece of dodo",
    "Homework",
    "Homework",
    "Sekiro: I die twice"
]



def winter_holiday(goodorbad:str) -> str:
    """give summary of winter break
        give good event if good
        give bad event if bad
    """
    if positivity == "good":
        return random.choice(goodlist)
    elif positivity == "bad":
        return random.choice(badlist)
print(winter_holiday(positivity))


#def main()->None:
    #winter_holiday(positivity)




#if __name__ == "__main__":
    #main()
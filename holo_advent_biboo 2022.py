# HOLOLIVE ADVENT BIBOO 2202
# BIBOO (Damien Cheng)
# SUS  
#Q1
fatty = 0
current = 0
with open("amongus_ADVENT_2022.txt") as f:
    for line in f:
        if line == '\n' :
            if current > fatty:
                fatty = current
            current = 0
        else:
            current = current + int(line)
print(fatty)








#Q2
best = 0
bestest = 0
bestestest = 0
current2 = 0
with open("amongus_ADVENT_2022.txt") as f:
    for line in f:
        if line == '\n' :
            if best < current2:
                best = current2
            
            elif bestest < current2:
                bestest = current2
            
            elif bestestest < current2:
                bestestest = current2
            current2 = 0
        else:
            current2 = current2 + int(line)
            
print(f"{best}, {bestest}, {bestestest}")
print(best + bestestest + bestest)
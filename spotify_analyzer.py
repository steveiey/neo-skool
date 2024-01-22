#sp data ana
# Damien
# Jan 16

#get all songs by drake

#use linear search

import csv

Drakesong = []


with open("./spotify.csv") as f:
    csv_reader = csv.DictReader(f)
    Drakesong = []
    for line in csv_reader:
        if "Drake" in line["artist"]:
            Drakesong.append((line["artist"], line["song_title"], line["danceability"]))



for i in range(len(Drakesong)):
    
    smol = Drakesong[i][-1]
    smoli = i
    
    for j in range(i+1, len(Drakesong)):
        
        if Drakesong[j][-1] < smol:
            smol + Drakesong[j][-1]
            smoli = j
    Drakesong[i], Drakesong[smoli] = (Drakesong[smoli], Drakesong[i])

for song in Drakesong:
    print(f"{song[1]}:\t\t{song[2]}")
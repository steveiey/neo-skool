import csv



with open("./spotify.csv") as f:

    csv_reader = csv.DictReader(f)

    drake_songs = []
    for line in csv_reader:
        if "drake" in line["artist"].lower():
            drake_songs.append(
                (line["artist"], line["song_title"], line["danceability"])
            )

for song in drake_songs:
    print(song)


for i in range(len(drake_songs)):

    smallest_danceability = drake_songs[i][-1]
    smallest_index = i

    for j in range(i + 1, len(drake_songs)):

        if drake_songs[j][-1] < smallest_danceability:
            smallest_danceability = drake_songs[j][-1]
            smallest_index = j
    drake_songs[i], drake_songs[smallest_index] = (
        drake_songs[smallest_index],
        drake_songs[i],
    )

print("--- Sorted Drake Songs by Danceability")
for song in drake_songs:
    print(f"{song[1]}:\t\t{song[2]}")
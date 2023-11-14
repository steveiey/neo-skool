# sim_score_sfu_best
# Damien Cheng
# Nov 10

# make algo that reads data and compares more than one person

#open .csv file
# use with open("")

similarest = 0
similarest_name = ""

leastest = 0
leastest_name = ""
#create a profile of likes
#convert data to list

#for item in profile
    #fi item in current line's 

profile = ["Starbucks", "Bamboo Gardenn", "Pizza Hut", "Guadalupe (MBC)", "Subway"]

with open("./data.csv") as f:
    for line in f:
        current_likes = line.split(",")
        current_name = current_likes[1]
        current_sim_score = 0
     
     
        for item in profile:
            if item in current_likes:
                current_sim_score += 1
        print(f"{current_name} - Score: {current_sim_score}")
        if current_sim_score > similarest:
            similarest_name = current_name
            similarest = current_sim_score
        if current_sim_score < similarest:
            leastest_name = current_name
            leastest = current_sim_score





print(f"most similar to {similarest_name}:{similarest}")
print(f"least similar to {leastest_name}:{leastest}")
#keep track of highest simularity score
#state top score + name


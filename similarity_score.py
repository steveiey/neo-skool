#similarity score
# damie cheng
# nov 9

# create two lists for different movies 
# compare the two

similarity_score = 1
ppl_fave_movie = ["matrix", "avengers", "infernal", "empires stike back", "rogue one"]

otherppl_fave_movie = ["amongus", "avengers", "sus", "rogue one"]

#compare +1 score if same movie

for movie in ppl_fave_movie:
    if movie in otherppl_fave_movie:
        similarity_score += 1
    

movie_titles=["TITLE1","TITLE2","TITLE3","TITLE4","TITLE5"]

file = open('movies.txt','w')
for title in movie_titles:
    file.write(title+"\n")
file.close()

import json 
from task1 import scrap_top_list
from task4 import scrap_movie_details
top_movies=scrap_top_list()
movie=top_movies[:50]
def get_movie_list_detail():
    l=[]
    for i in movie:
        for j in i:
            if j=="url":
                l.append(scrap_movie_details(i["url"]))
    f=open("task5.json","w")
    json.dump(l,f,indent=4)
    return l
get_movie_list_detail()
import json
from task5 import get_movie_list_detail
movie=get_movie_list_detail()
def analyse_movies_directors():
    d={}
    for i in movie:
        for j in i:
            if j=="director":
                k=i["director"]
                for m in k:
                    f=m
                    c=0
                    for a in movie:
                        for b in a:
                            if b=="director":
                                e=a["director"]
                                for g in e:
                                    if g==f:
                                        c=c+1
                    d[f]=c
    f=open("task7.json","w")
    json.dump(d,f,indent=4)
    return d
analyse_movies_directors()
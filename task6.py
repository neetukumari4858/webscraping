import json
from task5 import get_movie_list_detail
movie=get_movie_list_detail()
def analyse_movies_language():
    d={}
    for i in movie:
        for j in i:
            if j=="Language":
                k=i["Language"]
                for m in k:
                    f=m
                    c=0
                    for a in movie:
                        for b in a:
                            if b=="Language":
                                e=a["Language"]
                                for g in e:
                                    if g==f:
                                        c=c+1
                    d[f]=c
    f=open("task6.json","w")
    json.dump(d,f,indent=4)
    return d
analyse_movies_language()


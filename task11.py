import json
from task5 import get_movie_list_detail
movie=get_movie_list_detail()
def analyse_movies_genre():
    d={}
    for i in movie:
        for j in i:
            if j=="Genre":
                k=i["Genre"]
                for m in k:
                    f=m
                    c=0
                    for a in movie:
                        for b in a:
                            if b=="Genre":
                                e=a["Genre"]
                                for g in e:
                                    if g==f:
                                        c=c+1
                    d[f]=c
    f=open("task11.json","w")
    json.dump(d,f,indent=4)
    return d
analyse_movies_genre()


import json 
from task1 import scrap_top_list
movie=scrap_top_list()
def group_by_year():
    years=[]
    for k in movie:
        year=k["year"]
        if year not in years:
            years.append(year)
    dic={}
    for r in years:
        k=[]
        for p in movie:
            if r==p["year"]:
                k.append(p)
        dic[r]=k
    f=open("task2.json","w")
    json.dump(dic,f,indent=4)
    return dic
group_by_year()









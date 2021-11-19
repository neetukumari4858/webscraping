import json 
from task2 import group_by_year
scrap=group_by_year()
def group_by_decade(movie):
    movies_dic={}
    list1=[]
    for index in movie:
        last_no=index%10
        decade=index-last_no
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    
    for m in list1:
        movies_dic[m]=[]
    
    for i in movies_dic:
        h=i+9
        for x in movie:
            if x>=i and x<=h:
                for v in movie[x]:
                    movies_dic[i].append(v)
    f=open("task3.json","w")
    json.dump(movies_dic,f,indent=4)
group_by_decade(scrap)












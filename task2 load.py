import json 
f=open("task1.json","r+")
v=json.load(f)

def group_by_year(movie):
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
    f=open("task2load.json","w")
    json.dump(dic,f,indent=4)
    return dic
group_by_year(v)
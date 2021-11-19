import json 
import requests
from bs4 import BeautifulSoup
link="https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse"
def scrap_movie_details(link):
    d1={}
    page=requests.get(link)
    soup=BeautifulSoup(page.text,"html.parser")
    title_div=soup.find("h1",class_="scoreboard__title").get_text()
    d1["name"]=title_div
    a=soup.find_all("li",class_="meta-row clearfix")
    d1["link"]=link
    str=""
    for i in a:
        b=i.text
        d=b.split()
        for j in d:
            if j=="Rating:":
                d1["Rating"]=d[1]
            if "Genre:" in d:
                x=[]
                w=0
                while w<len(d):
                    if w==0:
                        w+=1
                        continue
                    x.append(d[w])
                    w+=1
                s=" "
                for i in x:
                    for j in i:
                        if j==" ":
                            continue
                        else:
                            z=","
                            if j=="&": 
                                x.remove(j)
                                s+=z
                            else:
                                s+=j
                l2=s.split(",")
                d1["Genre"]=l2
                # print(d1)
            if j=="Language:":
                d1.update({"Language":[d[-1]]})
            if "Director:" in d:
                l=[]
                i=0
                while i<len(d):
                    if i==0:
                        i+=1
                        continue
                    l.append(d[i])
                    i+=1
                s=""
                for i in l:
                    for j in i:
                        if j==" ":
                            continue
                        else:
                            s+=j
                l1=s.split(",")
                d1["director"]=l1
            if j=="Producer:":
                d1.update({"Producer":d[1:]})
            if j=="Runtime:":
                if "min" in d[1]:
                    a=int(d[1][0:-4])+int(d[2][0:2])
                else:
                    b=int(d[2][0:-1])
                    a=int(d[1][0])*60+b
                    
                d1.update({"Runtime":a})
    f=open("task4.json","w")
    json.dump(d1,f,indent=4)  
    return d1
scrap_movie_details(link)


import requests
import json 
from bs4 import BeautifulSoup
link="https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse"
def scrape_movie_cast():
    l=[]
    page=requests.get(link)
    soup=BeautifulSoup(page.text,"html.parser")
    div=soup.find(class_="castSection")
    for i in div:
        b=i.text
        d=b.split()
        for j in d:
            dic={}
            p=d[0]+d[1]
            dic["name"]=p
            if dic["name"] not in l:
                l.append(dic)
                break
    f=open("task12.json","w")
    json.dump(l,f,indent=4)
    return l
scrape_movie_cast()
    
    
    

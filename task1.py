import requests
import json 
from bs4 import BeautifulSoup
url="https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
req=requests.get(url)
html_content=req.text
soup=BeautifulSoup(html_content,"html.parser")
def scrap_top_list():
    l=[]
    main_div=soup.find("div",class_="body_main container")
    table=main_div.find("table",class_="table")
    tr=table.find_all("tr")
    for i in tr:
        d={}
        td=i.find_all("td")
        for j in td:
            rank=i.find("td",class_="bold").get_text()[:-1]
            d["rank"]=int(rank)
            rating=i.find("span",class_="tMeterScore").get_text()[:-1]
            a=float(rating)
            d["rating"]=a
            title=i.find("a",class_="unstyled articleLink")["href"][3:]
            d["title"]=str(title)
            reviews=i.find("td",class_="right hidden-xs").get_text()
            d["reviews"]=reviews
            year=i.find("a",class_="unstyled articleLink").text[-5:-1]
            d["year"]=int(year)   
            url="https://www.rottentomatoes.com/m/"+title
            d["url"]=url
            if d not in l:
                l.append(d)
            f=open("task1.json","w")
            json.dump(l,f,indent=4)
    return l
scrap=scrap_top_list()







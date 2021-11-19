import json
from task4 import scrap_movie_details
from task12 import scrape_movie_cast
url="https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse"
task4=scrap_movie_details(url)
task12=scrape_movie_cast()
def cast_detail():
    d=[]
    d.append(task4)
    for i in range(len(task12)):
        d.append(task12[i])
    f=open("task13.json","w+")
    json.dump(d,f,indent=4)
    return d   
cast_detail()



















# import json 
# import requests
# from task4 import scrap_movie_details
# from task12 import scrape_movie_cast
# scrap=scrap_movie_details()
# def scrap_movie_details():
#     url="https://www.rottentomatoes.com/m/toy_story_4"
    
#     req=requests.get(url)
#     r=req.text()
# print()

   

    


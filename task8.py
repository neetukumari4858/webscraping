# we have to made empty txt file for path like "movie.text"
import json 
import os
import requests
from task1 import scrap_top_list
scrap=scrap_top_list()
for  i in scrap:
    path="/home/admin123/web screping/movies.txt"+i["title"]+"text"
    if os.path.exists(path):
        pass
    else:
        create=open("/home/admin123/web screping/movies.txt"+i["title"]+"text","w")
        url=requests.get(i["url"])
        k=url.text
        create.write(k)
        create.close()


        
        

        
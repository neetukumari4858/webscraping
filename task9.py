import os
import random 
import time
import requests
from task5 import get_movie_list_detail
scrap=get_movie_list_detail()
for  i in scrap:
    random_sleep=random.randint(1,3)
    print(random_sleep)
    path="/home/admin123/web screping/movies.txt"+i["name"]+"text"
    if os.path.exists(path):
        pass
    else:
        p=str(i)
        create=open("/home/admin123/web screping/movies.txt"+i["name"]+"text","w")
        time.sleep(random_sleep)
        create.write(p)
        create.close()


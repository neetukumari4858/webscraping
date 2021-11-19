import json 
from task5 import get_movie_list_detail
movie=get_movie_list_detail()
def analyse_language_and_directors():
    dic={}
    for i in movie:
        for Director in i["director"]:
            dic[Director]={}
    for j in range(len(movie)):
        for Director in dic:
            if Director in movie[j]["director"]:
                for Language in movie[j]["Language"]:
                    dic[Director][Language]=0
    for j in range(len(movie)):
        for Director in dic:
            if Director in movie[j]["director"]:
                for Language in movie[j]["Language"]:
                    dic[Director][Language]+=1
                    

    task=open("task10.json","w")
    json.dump(dic,task,indent=4)
    return dic
print(analyse_language_and_directors())
    






   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   #     for director in dic:
    #         # print(director)
    #         if director in movie[j]["Director"]:
    #             for Language in movie[j]["Language"]:
    #                 dic["Director"]["Language"]=0
                    
    # for j in range(len(movie)):
    #     for director in dic:
    #         if director in movie[j]["director"]:
    #             for Language in movie[j]["Language"]:
    #                 dic["Director"]["Language"]=+1
    # f=open("task10.json","w")
    # json.dump(f,dic,indent=4)
    # return dic 
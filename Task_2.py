from Task_1 import screp_top_list
import json
import pprint
list_of_movies = screp_top_list()
# print(list_of_movies)
def name_of_year(movies):
    years=[]
    for i in movies:  
        year=i["year"]
        #print(i)
        if year not in years:
            years.append(year)
    years.sort()        
    movie_dict={i:[]for i in years}
    for i in movies:
        year=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
                with open("movie_year.json","w")as file:
                    json.dump(movie_dict,file,indent=4)
    return movie_dict
pprint.pprint(name_of_year(list_of_movies))    
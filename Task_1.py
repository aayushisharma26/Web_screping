from bs4 import BeautifulSoup
import requests
import json
import pprint
def screp_top_list(): 
    imdb_api="https://www.imdb.com/india/top-rated-indian-movies/"
    imdb_url=requests.get(imdb_api)
    Text_data=imdb_url.json
    soup=BeautifulSoup(imdb_url.text,"html.parser")
    list=[]
    
    div=soup.find("div",class_="lister")
    body=div.find("tbody",class_="lister-list")
    name=body.find_all("tr")
    number=0
    for i in name:
        number=number+1
        movie_name=i.find("td",class_="titleColumn").a.text
        year=i.find("td",class_="titleColumn").span.get_text()[1:5]
        year_in_int=int(year)
        rating=i.find("td",class_="ratingColumn").strong.get_text()
        rating_in_float=float(rating)
        url=i.find("td",class_="titleColumn").a["href"]
        my_dict={"possition":number,"name":movie_name,"year":year_in_int,"rating":rating_in_float,"url":("https://www.imdb.com")+url}
        list.append(my_dict)
    with open("my_file.json","w")as _data:
        json.dump(list,_data,indent=4)
    return(list)           
pprint.pprint(screp_top_list())





# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:50:57 2020

@author: admin
"""
with open('p3.txt','r') as file:
    dat=file.read()

from bs4 import BeautifulSoup
doc = dat

soup = BeautifulSoup(doc,'html.parser')

print soup.prettify()

zomato_div = soup.find_all('div',attrs={'class':'js-search-result-li'})





restaurant_type = []
restaurant_name = []
location = []
address = []
ratings = []
#first_ratings = []
#second_ratings = []
#first_review_count = []
#second_review_count = []
CUISINES = []
COST_FOR_TWO = []
HOURS = []
#info1 = []
#info2 = []
#info3 = []


movie_div = soup.find_all('div', class_='lister-item mode-advanced')

#our loop through each container
for container in zomato_div:

        all_res_type = []
        for a in container.find_all('div',attrs={'class':'mt5'}):
            print a.text
            all_res_type.append(a.text)
            
            
            
        restaurant_type.append(all_res_type)
            
        all_subzone = []
        for a in container.find_all('a', attrs={'class': 'search_result_subzone'}): 
            print a.text 
            all_subzone.append(a.text)
            
            
        location.append(all_subzone)
        
         
         #name
#        name = container.h3.a.text
#        titles.append(name)
        name = container.find('a', attrs={'class': 'result-title'}).text
        restaurant_name.append(name)
        
#        loc = container.find('a', attrs={'class': 'result-title'}).text
#        location.append(loc)
        
        all_address = []
        for a in container.find_all('div', attrs={'class': 'search-result-address'}): 
            print a.text 
            all_address.append(a.text)
            
        address.append(all_address) 
        
        #year
#        year = container.h3.find('span', class_='lister-item-year').text
#        years.append(year)

        # runtime
#        runtime = container.find('span', class_='runtime').text if container.p.find('span', class_='runtime').text else '-'
#        runtime.append(runtime)

        #IMDb rating
        nv1 = container.find_all('span', attrs={'class': 'rating-value'})
        rating1 = nv1[0].text
        #first_ratings.append(rating1)
        rating2 = nv1[1].text if len(nv1) > 1 else '-'
        #second_ratings.append(rating2)
        
        nv2 = container.find_all('span', attrs={'class': 'review-count'})
        review1 = nv2[0].text
        #first_review_count.append(review1)
        review2 = nv2[1].text if len(nv2) > 1 else '-'
        #second_review_count.append(review2)
        ratings.append(rating1+'-'+review1+','+rating2+'-'+review2)
        
        #imdb_ratings.append(imdb)
        
#        eat = container.find_all('a', attrs={'class': 'zdark'})
#        eat1 = eat[0].text
#        #first_eatable.append(eat1)
#        eat2 = eat[1].text if len(eat) > 1 else '-'
#        #second_review_count.append(eat2)
#        restaurant_type.append(eat1+','+eat2)
        
        cuisins_cost_text = []
        for a in container.find_all('span', attrs={'class':'col-s-11'}):
            print a.text
            cuisins_cost_text.append(a.text)
            
        CUISINES.append(cuisins_cost_text[0])
        COST_FOR_TWO.append(cuisins_cost_text[1])   
        
        
        all_time = []
        for a in container.find_all('div', class_='col-s-11'): 
           print a.text 
           all_time.append(a.text)   
        
        HOURS.append(all_time) 
#        cchf = float(container.find_all('span', attrs={'class': 'col-s-5'})
#        cchf0 = cchf[0].text
#        info0.append(cchf0)
#        cchf1 = cchf[1].text
#        info1.append(cchf1)
#        cchf2 = cchf[2].text
#        info2.append(cchf2)
#        cchf3 = cchf[3].text
#        info3.append(cchf3)
#        cchf4 = cchf[1].text if len(eat) > 1 else '-'
#        info4.append(cchf4)

import pandas as pd
import numpy as np
      
zomato = pd.DataFrame({
'restaurantType': restaurant_type,
'restaurantName': restaurant_name,
'timeMin': location,
'Address': address,
'ratings': ratings,
'cuisins': CUISINES,
'cost_for_two': COST_FOR_TWO,
'hours': HOURS
})


zomato.to_csv('zomato_data.csv')

        
var=[restaurant_type]#,'restaurant_name','location','address','ratings','CUISINES','COST_FOR_TWO','HOURS']
for i in var:
   print len(var[i]) 

len(restaurant_type)
len(restaurant_name)
len(location)
len(address)
len(ratings)
len(CUISINES)
len(COST_FOR_TWO)
len(HOURS)




        #metascore
#        m_score = container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-'
#        metascores.append(m_score)

        #there are two NV containers, grab both of them as they hold both the votes and the grosses
#        nv = container.find_all('span', attrs={'name': 'nv'})
#        
#        #filter nv for votes
#        vote = nv[0].text
#        votes.append(vote)
        
        #filter nv for gross
#        grosses = nv[1].text if len(nv) > 1 else '-'
#        us_gross.append(grosses)

#pandas dataframe        
#movies = pd.DataFrame({
#'movie': titles,
#'year': years,
#'timeMin': time,
#'imdb': imdb_ratings,
#'metascore': metascores,
#'votes': votes,
#'us_grossMillions': us_gross,
#})

#cleaning data 
movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
movies['timeMin'] = movies['timeMin'].str.extract('(\d+)').astype(int)
movies['metascore'] = movies['metascore'].astype(int)
movies['votes'] = movies['votes'].str.replace(',', '').astype(int)
movies['us_grossMillions'] = movies['us_grossMillions'].map(lambda x: x.lstrip('$').rstrip('M'))
movies['us_grossMillions'] = pd.to_numeric(movies['us_grossMillions'], errors='coerce')

#add dataframe to csv file named 'movies.csv'


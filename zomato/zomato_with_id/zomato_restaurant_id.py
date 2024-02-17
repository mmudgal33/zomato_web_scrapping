# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 21:02:43 2020

@author: admin
"""

# getting all restaurant_id

myfiles = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

restaurant_id = []


for i in myfiles:
    with open('p'+i+'.txt','r') as file:
        dat=file.read()



    from bs4 import BeautifulSoup
    doc = dat
    
    soup = BeautifulSoup(doc,'html.parser')
    
    print soup.prettify()
    
    #zomato_div = soup.find_all('div',attrs={'class':'js-search-result-li'})
    zomato_div = soup.find_all('div',attrs={'class':'card'})
    
    #zomato_div[0].prettify()
    
    #restaurant_id = []
    for container in zomato_div:
        for a in container.find_all("div" , class_="content"):
                idd = a.find_next('div')['data-res_id']
                restaurant_id.append(idd)

import pandas as pd
zomato_id = pd.DataFrame({
    'restaurantID': restaurant_id
    })
    

zomato_id.to_csv('zomato_id.csv')

zomato_union=pd.read_csv('zomato_union.csv')
zomato_union1=pd.concat([zomato_id,zomato_union],axis=1)

zomato_union1.to_csv('zomato_id_union.csv')
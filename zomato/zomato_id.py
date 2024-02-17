# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:45:47 2020

@author: admin
"""

from bs4 import BeautifulSoup
html='''<td class="measurement">
<div id="measurement_a000_20c0_0002">0.0</div>
</td>'''

soup=BeautifulSoup(html,"html.parser")
for item in soup.find_all("td" , class_="measurement"):
    print(item.find_next('div')['id'])
    
    
html='''
'''
soup=BeautifulSoup(html,"html.parser")


    
    
for item in soup.find_all("div" , class_="card"):    
    print(item.find_next('div')['data-res_id'])
       
    
    
soup.find_all("div" , class_="content")
###########################################################
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
    



########################################################################
#myfiles = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','p16','p17','p18','p19','p20']
myfiles = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']




for i in myfiles:
    with open('p'+i+'.txt','r') as file:
        dat=file.read()

    from bs4 import BeautifulSoup
    doc = dat
    
    soup = BeautifulSoup(doc,'html.parser')
    
    print soup.prettify()
    
    zomato_div = soup.find_all('div',attrs={'class':'card'})
    
    zomato_div[0].prettify()
    
    restaurant_id = []
    restaurant_type = []
    restaurant_name = []
    location = []
    address = []
    ratings = []
    CUISINES = []
    COST_FOR_TWO = []
    HOURS = []
    featured_1n = []
    #first_ratings = []
    #second_ratings = []
    #first_review_count = []
    #second_review_count = []
    
    
    
    #movie_div = soup.find_all('div', class_='lister-item mode-advanced')
    #len(movie_div)
    
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
            HOURS.append(all_time[0] if len(all_time)>0 else '-')
            featured_1n.append((all_time[1]) if len(all_time)>1 else '-')
            
            for a in container.find_all("div" , class_="js-search-result-li"):
                idd = a.find_next('div')['data-res_id']
                restaurant_id.append(idd)
            
    #        all_time = []
    #        for a in container.find_all('div', class_='col-s-11'): 
    #           print a.text 
    #           all_time.append(a.text)   
    #        
    #        HOURS.append(all_time) 
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
    
    import re
    
    mylist=HOURS
    timing1=[re.sub("[u'                                     ]","",elem) for elem in mylist] 
    timing=[re.sub("[^a-z0-9A-z:]",' ',elem) for elem in timing1]
    HOURS = timing
    
    mylist = restaurant_name
    restaurant_n=[re.sub("[^a-z0-9A-z:]",' ',elem) for elem in mylist]
    restaurant_nm=[re.sub("[                                     ']","",elem) for elem in restaurant_n] 
    restaurant_name = restaurant_nm
    
    mylist = featured_1n
    mylist_re=[re.sub("[^a-z0-9A-z:]",'',elem) for elem in mylist]
    featured_1n = mylist_re     
    
          
    
    zomato = pd.DataFrame({
    'restaurantType': restaurant_type,
    'restaurantName': restaurant_name,
    'location': location,
    'Address': address,
    'ratings': ratings,
    'cuisins': CUISINES,
    'cost_for_two': COST_FOR_TWO,
    'hours': HOURS,
    'featured_IN' : featured_1n,
    "restaurant_ID" : restaurant_id
    })

 
    
zomato.to_csv('zomato_p'+i+'.csv')
    
zomato_union=pd.concat([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20],axis=0)
zomato_union.to_csv('zomato_union.csv') 
zomato_union=zomato_union.drop(['hours'],axis=1)

data_FH=pd.read_csv('zomato_data_FH_union.csv')
zomato_union=pd.concat(['zomato_union','data_FH'],axis=1)

    
    
#k=p['restaurantName'].str.split('\r\r\n',expand=True)
#p['restaurantName']=k[0]
#
#p['Address']
#k=p['Address'].str.split("u' ",expand=True)
#p['Address']=k[1]
#
#p['ratings']

#len(restaurant_type)
#len(restaurant_name)
#len(location)
#len(address)
#len(ratings)
#len(CUISINES)
#len(COST_FOR_TWO)
#len(HOURS)
#len(featured_1n)
    



    
#zomato.to_csv('zomato_p1.csv')
#zomato.to_csv('zomato_p2.csv')
#zomato.to_csv('zomato_p3.csv')
#zomato.to_csv('zomato_p4.csv')
#zomato.to_csv('zomato_p5.csv')
#
#zomato.to_csv('zomato_p6.csv')
#zomato.to_csv('zomato_p7.csv')
#zomato.to_csv('zomato_p8.csv')
#zomato.to_csv('zomato_p9.csv')
#zomato.to_csv('zomato_p10.csv')
#
#zomato.to_csv('zomato_p11.csv')
#zomato.to_csv('zomato_p12.csv')
#zomato.to_csv('zomato_p13.csv')
#zomato.to_csv('zomato_p14.csv')
#zomato.to_csv('zomato_p15.csv')
#
#zomato.to_csv('zomato_p16.csv')
#zomato.to_csv('zomato_p17.csv')
#zomato.to_csv('zomato_p18.csv')
#zomato.to_csv('zomato_p19.csv')
#zomato.to_csv('zomato_p20.csv')
#
#p1=pd.read_csv('zomato_p1.csv')
#p2=pd.read_csv('zomato_p2.csv')
#p3=pd.read_csv('zomato_p3.csv')
#p4=pd.read_csv('zomato_p4.csv')
#p5=pd.read_csv('zomato_p5.csv')
#
#p6=pd.read_csv('zomato_p6.csv')
#p7=pd.read_csv('zomato_p7.csv')
#p8=pd.read_csv('zomato_p8.csv')
#p9=pd.read_csv('zomato_p9.csv')
#p10=pd.read_csv('zomato_p10.csv')
#
#p11=pd.read_csv('zomato_p11.csv')
#p12=pd.read_csv('zomato_p12.csv')
#p13=pd.read_csv('zomato_p13.csv')
#p14=pd.read_csv('zomato_p14.csv')
#p15=pd.read_csv('zomato_p15.csv')
#
#p16=pd.read_csv('zomato_p16.csv')
#p17=pd.read_csv('zomato_p17.csv')
#p18=pd.read_csv('zomato_p18.csv')
#p19=pd.read_csv('zomato_p19.csv')
#p20=pd.read_csv('zomato_p20.csv')



       

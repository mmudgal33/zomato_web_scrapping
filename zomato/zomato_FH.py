# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 19:47:49 2020

@author: admin
"""


with open('p16.txt','r') as file:
    dat=file.read()

from bs4 import BeautifulSoup
doc = dat

soup = BeautifulSoup(doc,'html.parser')

print soup.prettify()

zomato_div = soup.find_all('div',attrs={'class':'js-search-result-li'})
len(zomato_div)


featured_1n = []
HOURS = []


for container in zomato_div:        
        all_time = []
        for a in container.find_all('div', class_='col-s-11'):
            print a.text 
            all_time.append(a.text)
            HOURS.append(all_time[0])
            featured_1n.append((all_time[1]) if len(all_time)>1 else '-')
            
for container in zomato_div:
    for a in container.find_all('div', class_='col-s-11'):
        print a
        
container.find_all('div', class_='col-s-11')

x= {1:5}
for i in len(zomato_div):
    zomato_div[1].find_all('div', class_='col-s-11')

import re

mylist=HOURS

timing1=[re.sub("['\n                                    ]","",elem) for elem in mylist] 
#timing1=[re.sub("[\u]",'',elem) for elem in timing] 

#[a-zA-Z0-9_]
timing=[re.sub("[^a-z0-9A-z:]",' ',elem) for elem in timing1]
#str = re.sub(r' [^a-z0-9]+ ', ' ', str)
#HOURS = timing

mylist1=featured_1n
featured_1n=[re.sub("[^a-z0-9A-z:]",' ',elem) for elem in mylist1]




import pandas as pd
import numpy as np
      
zomato = pd.DataFrame({
'featuredIN': featured_1n,
'hours': timing
})


zomato.to_csv('zomato_data_FH20.csv')

        

len(featured_1n)
len(timing)

p1=pd.read_csv('zomato_data_FH1.csv')
p2=pd.read_csv('zomato_data_FH2.csv')
p3=pd.read_csv('zomato_data_FH3.csv')
p4=pd.read_csv('zomato_data_FH4.csv')
p5=pd.read_csv('zomato_data_FH5.csv')

p6=pd.read_csv('zomato_data_FH6.csv')
p7=pd.read_csv('zomato_data_FH7.csv')
p8=pd.read_csv('zomato_data_FH8.csv')
p9=pd.read_csv('zomato_data_FH9.csv')
p10=pd.read_csv('zomato_data_FH10.csv')

p11=pd.read_csv('zomato_data_FH11.csv')
p12=pd.read_csv('zomato_data_FH12.csv')
p13=pd.read_csv('zomato_data_FH13.csv')
p14=pd.read_csv('zomato_data_FH14.csv')
p15=pd.read_csv('zomato_data_FH15.csv')

p16=pd.read_csv('zomato_data_FH16.csv')
p17=pd.read_csv('zomato_data_FH17.csv')
p18=pd.read_csv('zomato_data_FH18.csv')
p19=pd.read_csv('zomato_data_FH19.csv')
p20=pd.read_csv('zomato_data_FH20.csv')


zomato_union=pd.concat([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p17,p18,p19,p20],axis=0)
zomato_union.to_csv('zomato_data_FH_union.csv')





timing[20]


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


k=p['restaurantName'].str.split('\r\r\n',expand=True)
p['restaurantName']=k[0]

p['Address']
k=p['Address'].str.split("u' ",expand=True)
p['Address']=k[1]

p['ratings']


hours,

    
zomato.to_csv('zomato_p1.csv')
zomato.to_csv('zomato_p2.csv')
zomato.to_csv('zomato_p3.csv')
zomato.to_csv('zomato_p4.csv')
zomato.to_csv('zomato_p5.csv')

zomato.to_csv('zomato_p6.csv')
zomato.to_csv('zomato_p7.csv')
zomato.to_csv('zomato_p8.csv')
zomato.to_csv('zomato_p9.csv')
zomato.to_csv('zomato_p10.csv')

zomato.to_csv('zomato_p11.csv')
zomato.to_csv('zomato_p12.csv')
zomato.to_csv('zomato_p13.csv')
zomato.to_csv('zomato_p14.csv')
zomato.to_csv('zomato_p15.csv')

zomato.to_csv('zomato_p16.csv')
zomato.to_csv('zomato_p17.csv')
zomato.to_csv('zomato_p18.csv')
zomato.to_csv('zomato_p19.csv')
zomato.to_csv('zomato_p20.csv')

p1=pd.read_csv('zomato_p1.csv')
p2=pd.read_csv('zomato_p2.csv')
p3=pd.read_csv('zomato_p3.csv')
p4=pd.read_csv('zomato_p4.csv')
p5=pd.read_csv('zomato_p5.csv')

p6=pd.read_csv('zomato_p6.csv')
p7=pd.read_csv('zomato_p7.csv')
p8=pd.read_csv('zomato_p8.csv')
p9=pd.read_csv('zomato_p9.csv')
p10=pd.read_csv('zomato_p10.csv')

p11=pd.read_csv('zomato_p11.csv')
p12=pd.read_csv('zomato_p12.csv')
p13=pd.read_csv('zomato_p13.csv')
p14=pd.read_csv('zomato_p14.csv')
p15=pd.read_csv('zomato_p15.csv')

p16=pd.read_csv('zomato_p16.csv')
p17=pd.read_csv('zomato_p17.csv')
p18=pd.read_csv('zomato_p18.csv')
p19=pd.read_csv('zomato_p19.csv')
p20=pd.read_csv('zomato_p20.csv')


zomato_union=pd.concat([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p17,p18,p19,p20],axis=0)
zomato_union.to_csv('zomato_union.csv') 

       
p=pd.read_csv('zomato_union.csv')

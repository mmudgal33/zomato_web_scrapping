# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 00:50:47 2020

@author: admin
"""
# https://realpython.com/beautiful-soup-web-scraper-python/
#f=open('D:/mohit gate/edvancer python/zomatoWS/zomato.html','r')

#text=""
#for line in f:
#    #if line.strip()=="":continue   #remove blank lines else single text without \n
#    #else:
#        text+=''+line.strip()
#print(text)
#f.close()

with open('zomato.txt','r') as file:
    dat=file.read()

from bs4 import BeautifulSoup
doc = dat

soup = BeautifulSoup(doc,'html.parser')

print soup.prettify()
#results = soup.find_all('span',attrs={"class":"review-count medium"})
#len(results)
#results[0:3]
#
#results = soup.find_all('div',attrs={'class':'res-timing clearfix'})
#len(results)
#
#
#results = soup.find_all('div',attrs={'class':'row'})
#len(results)
#print results[0:5]
#results = soup.find_all('a',attrs={'title':'Sweet Shops in Agra'})
#len(results)
#
#sweetshop = soup.find_all('a', attrs={'title':'Sweet Shops in Agra'})
#len(sweetshop)

results = soup.find_all('div',attrs={'class':'col-s-12'})
len(results)
print results[0:5]
print results[-1]











div class="js-search-result-li even  status 1"


<div class="content">

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')

print(results.prettify())

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    print(job_elem, end='\n'*2)
    

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    print(title_elem)
    print(company_elem)
    print(location_elem)
    print()
    
    
    
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    print(title_elem.text)
    print(company_elem.text)
    print(location_elem.text)
    print()
    
    
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
    
    
python_jobs = results.find_all('h2', string='Python Developer')

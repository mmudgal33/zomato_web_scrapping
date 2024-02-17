# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:47:39 2020

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

with open('p3.txt','r') as file:
    dat=file.read()

from bs4 import BeautifulSoup
doc = dat

soup = BeautifulSoup(doc,'html.parser')

print soup.prettify()

#zom = soup.prettify()
#file1 = open("zomm.txt","a") 
#file1.write(zom)
#file1.close()
#
#
#zom.to_('zomm.txt')
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

results = soup.find_all('div',attrs={'data-res_id':'*'})
len(results)
print results[0:5]
print results[-1]

zomato_div = soup.find_all('div',attrs={'class':'js-search-result-li'})
len(zomato_div)
print zomato_div[0:5]
print zomato_div[-1]

for container in zomato_div:

        #name
        name = container.h3.a.text
        titles.append(name)
        
        #year
        year = container.h3.find('span', class_='lister-item-year').text
        years.append(year)

        # runtime
        runtime = container.p.find('span', class_='runtime').text if container.p.find('span', class_='runtime').text else '-'
        time.append(runtime)

        #IMDb rating
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)

        #metascore
        m_score = container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-'
        metascores.append(m_score)

        #there are two NV containers, grab both of them as they hold both the votes and the grosses
        nv = container.find_all('span', attrs={'name': 'nv'})
        
        #filter nv for votes
        vote = nv[0].text
        votes.append(vote)
        
        #filter nv for gross
        grosses = nv[1].text if len(nv) > 1 else '-'
        us_gross.append(grosses)



 <div class="rating-div ">
href="https://www.zomato.com/agra/shahganj-restaurants"



for p in soup.select('p'):
    if p['id'] == 'walrus':
        print(p.text)




from requests import get
from bs4 import BeautifulSoup
raw_html = open('contrived.html').read()
html = BeautifulSoup(raw_html, 'html.parser')
for p in html.select('p'):
    if p['id'] == 'walrus':
        print(p.text)
    
        




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

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:15:29 2020

@author: admin
"""

"""
<div class="js-search-result-li even status 1" data-position="3-15" data-res_id="3401310" data-trprovider="">
<article class="search-result ">
<div class="pos-relative clearfix ">
<div class="row">
<div class="col-s-6 col-m-4">
<div class="search_left_featured clearfix">
<a class="feat-img lazy" data-original="https://b.zmtcdn.com/data/pictures/0/3401310/3e7ffce6095597df132109c9cfe803f3_featured_v2.jpg?fit=around
%7C200%3A200&amp;crop=200%3A200%3B%2A%2C%2A" href="https://www.zomato.com/agra/shree-balaji-family-restaurant-sikandra/info" style="  background-image:url
(https://b.zmtcdn.com/images/placeholder_200.png);background-repeat: repeat;"></a>
</div>
</div>
<div class="col-s-16 col-m-12 pl0 ">
<div class="row">
<div class="col-s-12">
<div class="res-snippet-small-establishment mt5" style="margin-bottom: 7px;"><a class="zdark ttupper fontsize6" href="https://www.zomato.com/agra/quick-bites " title="Quick Bites 
in Agra">Quick Bites</a></div>
<a class="result-title hover_feedback zred bold ln24 fontsize0 " data-result-type="ResCard_Name" href="https://www.zomato.com/agra/shree-balaji-family-restaurant-sikandra" 
title="shree balaji family restaurant Restaurant, Sikandra">Shree Balaji Family Restaurant
                                    </a>
<div class="flex align-center both-rating">
<div class="rating-div ">
<div class="star " data-icon="" style="color:#1C1C1C"></div>
<span class="rating-value ">4.0</span>
<span class="review-count medium">(347)</span>
</div>
<span class="pipe ">|</span>
<div class="rating-div ">
<div class="star " data-icon="" style="color:#E23744"></div>
<span class="rating-value ">3.8</span>
<span class="review-count medium">(11.7K)</span>
</div>
</div>
<div class="clear"></div>
<a class="ln24 search-page-text mr10 zblack search_result_subzone left" href="https://www.zomato.com/agra/sikandra-restaurants" title="Restaurants in 
Sikandra"><b>Sikandra</b></a>
</div>
<div class="ta-right floating search_result_rating col-s-4 clearfix" style="line-height: 14px;">
</div>
</div>
<div class="row">
<div class="col-m-16 search-result-address grey-text nowrap ln22" style=" max-width:370px; " title="Paschim Puri, Sulabh Puram Colony, Sikandra, Agra"> Paschim Puri, Sulabh 
Puram Colony, Sikandra, Agra</div>
</div>
</div>
</div>
</div>
<div class="ui divider"></div>
<div class="search-page-text clearfix row">
<div class="clearfix"><span class="col-s-5 col-m-4 ttupper fontsize5 grey-text">Cuisines: </span><span class="col-s-11 col-m-12 nowrap pl0"><a 
href="https://www.zomato.com/agra/restaurants/biryani" title="Biryani">Biryani</a>, <a href="https://www.zomato.com/agra/restaurants/north-indian" title="North Indian">North 
Indian</a>, <a href="https://www.zomato.com/agra/restaurants/mughlai" title="Mughlai">Mughlai</a>, <a href="https://www.zomato.com/agra/restaurants/awadhi" 
title="Awadhi">Awadhi</a>, <a href="https://www.zomato.com/agra/restaurants/beverages" title="Beverages">Beverages</a></span></div>
<div class="res-cost clearfix"><span class="col-s-5 col-m-4 ttupper fontsize5 grey-text">Cost for two:</span><span class="col-s-11 col-m-12 pl0">Rs. 400</span></div>
<div class="res-timing clearfix" title="11 AM to 11 PM">
<span class="col-s-5 col-m-4 ttupper fontsize5 grey-text left">Hours:</span>
<div class="col-s-11 col-m-12 pl0 search-grid-right-text ">
                                    11am – 11pm (Mon-Sun)
                                                                    </div>
<div class="clear"></div>
</div>
</div>
</article>
</div>
"""

with open('p3.txt','r') as file:
    dat=file.read()

from bs4 import BeautifulSoup
doc = dat

soup = BeautifulSoup(doc,'html.parser')

print soup.prettify()


zomato_div = soup.find_all('div',attrs={'class':'js-search-result-li'})
len(zomato_div)
print zomato_div[0:5]
print zomato_div[-1]

zomato_div[-1].prettify()

name = zomato_div[-1].div.a.text
len(name)
year = movie_div[-1].div.find('a', class_='href').text






zomato_div[-1].prettify()
#<h3 class="lister-item-header">
#        <span class="lister-item-index unbold text-primary">50.</span>
#    
#    <a href="/title/tt0109830/?ref_=adv_li_tt"
#>Forrest Gump</a>

name = movie_div[-1].h3.a.text

#<span class="lister-item-year text-muted unbold">(1994)</span>
year = zomato_div[-1].h1.find('span', class_='lister-item-year').text

year = zomato_div[-1].find('span', class_='lister-item-year').text

#<p class="text-muted ">
#            <span class="certificate">12</span>
#                 <span class="ghost">|</span> 
#                <span class="runtime">142 min</span>
#                 <span class="ghost">|</span> 
#            <span class="genre">
#Drama, Romance            </span>
#    </p>

runtime = movie_div[-1].p.find('span', class_='runtime').text if movie_div[-1].p.find('span', class_='runtime').text else '-'

runtime = zomato_div[-1].find('span', class_='col-s-5 col-m-4').text if zomato_div[-1].div.find('span', class_='a').text else '-'
z1=zomato_div[-1].find('span', class_='a')
#######################################################

zomato_div[-1].find_all('div',attrs={'class':'rating-div'})
#rv=zomato_div[-1].find('span',attrs={'class':'rating-value'}).text
#rc=zomato_div[-1].find('span',attrs={'class':'review-count'}).text
#rc=zomato_div[-1].find('span',attrs={'class':'review-count'}).text

rt = zomato_div[-1].find_all('span', attrs={'class': 'rating-value'})
rc = zomato_div[-1].find_all('span', attrs={'class': 'review-count'})
        
        #filter rt for rating-value
        rating0 = rt[0].text
        rating1 = rt[1].text
        review0 = rc[0].text
        review1 = rc[1].text
rating0,rating1,review0,review1
#######################################################

zomato_div[-1].find_all('a',attrs={'class':'ln24'})

resto1 = zomato_div[-1].find('a', attrs={'class': 'result-title'}).text
resto2 = zomato_div[-1].find('a', attrs={'class': 'search_result_subzone'}).text
resto1,resto2

all_subzone = []
for a in zomato_div[-2].find_all('a', attrs={'class': 'search_result_subzone'}): 
    print a.text 
    all_subzone.append(a.text)

#######################################################

zomato_div[-1].find_all('div',attrs={'class':'mt5'})
eat = zomato_div[-1].find_all('a', attrs={'class': 'zdark'})
eat0 = eat[0].text
eat1 = eat[1].text if len(eat) > 1 else '-'

#runtime = zomato_div[-2].find_all('a', attrs={'class': 'zdark'}).text if zomato_div[-2].find_all('a', attrs={'class': 'zdark'}) else '-'
#        time.append(runtime)

all_res_type = []
for a in zomato_div[-2].find_all('div',attrs={'class':'mt5'}): 
    print a.text 
    all_res_type.append(a.text)
    
    
res_t0 = all_res_type[0]
res_t1 = all_res_type[1]
res_t2 = all_res_type[2]
res_t3 = all_res_type[3]


########################################################

zomato_div[-1].find_all('div',attrs={'class':'col-m-16'})
address = zomato_div[-1].find('div', attrs={'class': 'search-result-address'}).text
address

all_address = []
for a in zomato_div[-2].find_all('div', attrs={'class': 'search-result-address'}): 
    print a.text 
    all_address.append(a.text)

###########################################################

zomato_div[-1].find_all('span',attrs={'class':'col-s-5'})
cch = zomato_div[-2].find_all('span', attrs={'class': 'col-s-5'})
cch[0].text
cch[1].text
cch[2].text
cch[3].text if len(cch) > 2 else '-'
cch[0].text,cch[1].text,cch[2].text
############################################################

zomato_div[-1].find_all('span',attrs={'class':'col-s-11'})
dish = zomato_div[-1].find_all('span', attrs={'class': 'nowrap'}).text
dish[0].text
dishes = zomato_div[-1].find_all('span', class_='col-s-11')
fir=dishes
dishes.find_all('a','href').text

dish=zomato_div[-1].find_all('span',attrs={'class':'col-s-11'})
dishes = zomato_div[-1].find_all('a',attrs={'title'})#, class_='col-s-11')
dishes[0]

zomato_div[-1].find_all('a', href=True)

links_with_text = []
for a in zomato_div[-1].find_all('a', href=True): 
    if a.text: 
        links_with_text.append(a['href'])
        
all_text = []
for a in zomato_div[-1].find_all('a', href=True): 
    print a.text 
    all_text.append(a.text)


all_text = []
for a in zomato_div[-1].find_all('span', attrs={'class':'col-s-11'}): 
    print a.text 
    all_text.append(a.text)

all_text[5:8]

#all_text
#Out[298]: 
#[u'',
# u'Bar',
# u'Casual Dining',
# u'Kiskey Whiskey\n                                    ',
# u'Civil Lines',
# u'North Indian',
# u'Continental',
# u'Chinese',
# u'Great Food, No Bull']
##############################################################

#zomato_div[-1].find_all('span',attrs={'class':'col-s-5'})
#cch = zomato_div[-1].find_all('span', attrs={'class': 'col-s-5'})


################################################################
zomato_div[-1].find_all('div',attrs={'class':'res-timing'})
res_timing = zomato_div[-1].find_all('span', attrs={'class': 'grey-text'})
len(res_timing)
restime=zomato_div[-1].find_all('div',attrs={'class':'res-timing'})
#restime.find_all('span').text

runtime = zomato_div[-1].find_all('div', class_='col-s-11')
runtime[1].text

all_time = []
for a in zomato_div[10].find_all('div', class_='col-s-11'): 
    print a.text 
    all_time.append(a.text)
    
all_time[0],all_time[1]
    

for container in zomato_div:
    
    

featured_1n = []
HOURS = []
for container in zomato_div:
    all_time = []
    for a in container.find_all('div', class_='col-s-11'):
        print a.text 
        all_time.append(a.text)
        
        

        
        
        
HOURS.append(all_time[0])
HOURS.append(all_time[1] if len(all_time)>1)
        
           
    


####################################################################

#<strong>
#     8.8
#    </strong>
imdb = float(movie_div[-1].strong.text)



#<span class="metascore favorable">
#     82
#    </span>
#    Metascore
m_score = movie_div[-1].find('span', class_='metascore').text if movie_div[-1].find('span', class_='metascore') else '-'


#<span data-value="1742884" name="nv">
#    1,742,884
#   </span>
nv = movie_div[-1].find_all('span', attrs={'name': 'nv'})
#<span data-value="1742884" name="nv">1,742,884</span>,
# <span data-value="330,252,182" name="nv">$330.25M</span>        
        #filter nv for votes
        vote = nv[0].text
        
        
        
        
        
grosses = nv[1].text if len(nv) > 1 else '-'   







titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')

#our loop through each container
for container in movie_div:

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

#pandas dataframe        
movies = pd.DataFrame({
'movie': titles,
'year': years,
'timeMin': time,
'imdb': imdb_ratings,
'metascore': metascores,
'votes': votes,
'us_grossMillions': us_gross,
})

#cleaning data 
movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
movies['timeMin'] = movies['timeMin'].str.extract('(\d+)').astype(int)
movies['metascore'] = movies['metascore'].astype(int)
movies['votes'] = movies['votes'].str.replace(',', '').astype(int)
movies['us_grossMillions'] = movies['us_grossMillions'].map(lambda x: x.lstrip('$').rstrip('M'))
movies['us_grossMillions'] = pd.to_numeric(movies['us_grossMillions'], errors='coerce')

#add dataframe to csv file named 'movies.csv'
movies.to_csv('movies.csv')
















# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

import pip
pip.__main__(['install','urllib'])
pip.install "urllib"


from urllib3.request import urlopen
x=urlopen('https://www.zomato.com/agra/restaurants')
k=x.read()

import requests
r=requests.get('https://www.zomato.com/agra/restaurants')
r.text[:200]

# 34.82.236.211  3128

import urllib3
from bs4 import BeautifulSoup
http=urllib3.PoolManager()
r=http.request('GET','https://www.zomato.com/agra/restaurants/')
soup=BeautifulSoup(dat.data,'lxml')
print(soup.title)
print(soup.title.text)

import pandas as pd
import numpy as np

path=r"C:/mohit/"
f=open('C:/mohit/zomato.txt','r')
f.text[:200]
f

with open('zomato.txt','r') as file:
    dat=file.read()#.replace('\n','')

url=urllib3.request_encode_url('POST',dat)
   
dat[:]

print(data)


from bs4 import BeautifulSoup
mydata=requests.get(data).read

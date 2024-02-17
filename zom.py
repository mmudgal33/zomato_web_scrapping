# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:18:02 2020

@author: admin
"""

import pandas as pd
import numpy as nm


import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()

zm = "D:/mohit gate/edvancer python/zomatoWS/zomato.html"
#Query the website and return the html to the variable 'page'
r = http.request('GET', 'https://authoraditiagarwal.com')
r = http.request('GET', "D:/mohit gate/edvancer python/zomatoWS/zomato.html")


soup = BeautifulSoup(r.text,'html.parser')

f=open("D:/mohit gate/edvancer python/zomatoWS/zomato.txt",'r')


file = codecs.open("zomato.html", "r", "utf-8")
print(file.read())

f=open("D:/mohit gate/edvancer python/zomatoWS/zomato.txt",'r')
text=""
for line in f:
    if line.strip()=="":continue   #remove blank lines else single text without \n
    else:
        text+=''+line.strip()
print(text)
f.close()



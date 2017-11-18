# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 22:47:33 2017

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import re

r = requests.get("http://quote.eastmoney.com/stocklist.html")
r.encoding = r.apparent_encoding

soup = BeautifulSoup(r.text, "html.parser")
a = soup.find_all('a')
for i in a:
    try:
        lst = []
        href = i.attrs['href']
        lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        print (lst)
    except:
        continue
        
        
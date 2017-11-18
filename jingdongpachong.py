# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 19:45:46 2017

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import re
import math

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "cont"
    
def fillList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for i in range(25):
        ulist.append(soup.find_all('strong',{'class':re.compile('J_\d{7}')})[i].text)
    return ulist

def main():
    maclist = []
    url = "https://search.jd.com/Search?keyword=macbook%20pro&enc=utf-8&suggest=1.def.0.V12&wq=macb&pvid=a527b3aa8e1b4ad4ba2a1d936b7c0aed"
    html = getHTMLText(url)
    maclist = fillList(maclist, html)
    for i in range(25):
        print(maclist[i])
    print(type(maclist[0]))
    
    
    
main()
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:45:53 2017

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
        r = requests.get(url, headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
  
def main():
    
    url = "http://www.xicidaili.com/nn/"
    html = getHTMLText(url)
    IP = re.findall(r'\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?', html)
    
    print ("IP-Address")
    for i in range(len(IP)):
        print (IP[i])

    soup = BeautifulSoup(html, "html.parser")  
    a = soup.find_all('a',{'href' : re.compile(r'\/\d\d\d\d\-\d\d?\-\d\d?\/\w\w\w\w\w\w?\w?\w?\w?\w?\w?\w?\w?') })    
    for j in range(len(a)):
       print (a[j].text)
       

main()
    
    
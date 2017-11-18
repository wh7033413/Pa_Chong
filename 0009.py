# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 21:29:06 2017

@author: Administrator
"""

import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
def fillMovList(flist, html, ):
    try:
        flist = re.findall(r'title\=\".*?\"', html)
        print(len(flist))
        for i in range(len(flist)):
            ulist = eval(flist[i].split('=')[1])
            print(ulist)
        
    except:
        return ""
    
   

def main():
    uinfo = []    
    url = 'https://movie.douban.com/chart'
    html = getHTMLText(url)
    fillMovList(uinfo, html)
   
    
main()
            

            
    
    
    
    
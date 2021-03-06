# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 10:31:20 2017

@author: Administrator
"""
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[9].string])
        
def printUnivList(ulist, num):
    print("{:^10}\t{:^10}\t{:^10}".format("rank", "shool", "score"))
    for i in range (num):
        u = ulist[i]
        print("{:^10}\t{:^10}\t{:^10}".format(u[0], u[1], u[2]))

def main():
    info = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(info, html)
    printUnivList(info, 20)
    
main()



        
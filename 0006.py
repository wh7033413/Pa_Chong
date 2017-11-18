#-*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import bs4

def getHTMLText(url):
	try:
		r = requests.get(url)
		r.raise_for_stauts()
		r.encoding = r.append_encoding
		return r.text

	except:
		return ""

	

def fillUnivList(ulist, html):
	soup = BeautifulSoup(html, "html.parser")
	for tr in soup.find('tbody').childre:
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td')
			ulist.append([tds[0].string, tds[1].string],tds[3].string)

def printUnivList(ulist, num):
	print("{:^10}\t{:^10}\t{:^10}").format("rank", "scholl", "score")
	for i in range(num):
		u = ulist[i]
		print("{:^10}\t{:^10}\t{:^10}").format(u[0], u[1], u[3])

def main():
	uinfo = []
	url = "http://www.zuihaodaxue.cn/shengyuanzhiliangpaiming2017.html"
	html = getHTMLText(url)
	fillUnivList(uinfo, html)
	printUnivList(uinfo, 20)

main()
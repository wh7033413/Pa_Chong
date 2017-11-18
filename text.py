from bs4 import BeautifulSoup
import re
import requests

def getHTMLText(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.coding = 'utf-8'
		return r.text
	except:
		return ""

def getBookList(BookList, newBook, html):
	soup = BeautifulSoup(html, "html.parser")
	alist = soup.find_all('a', attrs={'href':re.compile(r'https\:\/\/book\.douban\.com\/subject\/\d{7}\d?\/')})
	for i in range(len(alist)):			
		BookList.append(alist[i].text)
	BookList = BookList[1:len(BookList):2]
	for i in range(len(BookList)):
		newBook.append(BookList[i].split()[0])

	return newBook

'''def getBookList(ulist, html):
	soup = BeautifulSoup(html, "html.parser")
	a = soup.find_all('a', attrs = {'href':re.compile(r'https\:\/\/book\.douban\.com\/subject\/\d{7}\/')})
	for i in range(len(a)):
		ulist.append(a[i].text)
	ulist = ulist[1:len(ulist):2]
	return ulist '''
	


		
	

def printBookList(ulist):
	print (ulist)

def mian():
	BookList = []
	newBook = []
	
	url = "https://www.douban.com/doulist/38391562/"	
	html = getHTMLText(url)
	getBookList(BookList, newBook, html)
	print (newBook)
	'''soup = BeautifulSoup(html, "html.parser")
	alist = soup.find_all('a', attrs={'href':re.compile(r'https\:\/\/book\.douban\.com\/subject\/\d{7}\d?\/')})
	for i in range(len(alist)):			
		BookList.append(alist[i].text)
	BookList = BookList[1:len(BookList):2]
	for i in range(len(BookList)):
		newBook.append(BookList[i].split()[0])
	print (newBook)
	print (len(newBook))'''


mian()

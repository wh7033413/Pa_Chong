#爬取网页的通用代码框架
#-*- coding: UTF-8 -*-

import requests

def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status() #如果状态不是200，引发HTTPErorr异常
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "产生异常"
	
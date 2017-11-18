#-*- coding: UTF-8 -*-

import requests

path = 'D://ab.jpg'
url = "http://script.zxxk.com/flash/js1709203.jpg"
r = requests.get(url)
r.status_code
print(r.status_code)

with open(path, 'wb') as f:
	f.write(r.content)


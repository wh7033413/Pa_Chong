#-*- coding: UTF-8 -*-

import requests

url = "http://www.ip138.com/ips138.asp?ip=123.181.9.61&action=2"
r = requests.get(url)
r.encoding = r.apparent_encoding
print(r.status_code)
print(r.text[0:1000])
#-*- coding: UTF-8 -*-

import requests
r = requests.get("http://www.baidu.com")
print(r.status_code) #HTTP 请求返回状态，200表示链接成功，404表示链接失败
print(r.text)        #HTTP 响应内容的字符串形式，即，url对应的页面内容
print(r.encoding)



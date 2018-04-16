#!usr/bin/env python
# coding:utf8

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import urllib
import urllib2

import json
from bs4 import BeautifulSoup




# GET
# url = 'http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&year=2013'
# request = urllib2.Request(url=url)
# response =urllib2.urlopen(request,timeout=20)
# result = unicode(response.read())
# print result


# POST
# url = 'http://shuju.wdzj.com/depth-data.html'
# data = urllib.urlencode({
#     'target': 19,
#     'target': 20,
#     'type': 0,
#     'wdzjPlatId': 59
# })
# request = urllib2.Request(url)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
# response = opener.open(request,data)
# result = response.read()
#
# print result


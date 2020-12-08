from datetime import datetime
import time,requests
from bs4 import BeautifulSoup
# print(time.mktime(datetime.now().timetuple()))
# print(time.time())
# # print(datetime.fromtimestamp(time.time()).strftime("%A, %B %d, %Y %I:%M:%S"))

# import os
# import django

# os.environ['DJANGO_SETTINGS_MODULE'] = 'assets.settings'
# django.setup()

# from root.models import *

# itemontop = TEST.objects.all().order_by('-id')
# for x in itemontop:
#     print(x)

# x = requests.get('https://unityassets4free.com/weapons/')

# soup = BeautifulSoup(x.text,'lxml')
# soup = soup.find_all("article",attrs={ "class" : "elementor-post" })[-1]

# print(soup.find('a').get('href'))

# x = requests.get('https://unityassets4free.com/monsters-ultimate-pack-01-cute-series/2/')

# soup = BeautifulSoup(x.text,'lxml')
# soup = soup.find_all("table")[0].find('a').get('href')
# print(soup)
# print(soup.find('img').get('src'))


x = ['212 **', "how ** to download", '** presave']
import random
random.shuffle(x)
x = [x.replace('**', 'query') for x in x]
print(x)


#
# test






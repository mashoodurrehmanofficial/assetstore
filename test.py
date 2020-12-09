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

# x = requests.get('https://assetstore.unity.com/packages/tools/game-toolkits/adventure-creator-11896')
# soup = BeautifulSoup(x.text,'lxml')
# soupdes = BeautifulSoup(x.text,'lxml').find(nonce='ZRO5bbOK9tVpUzSW')
# soup = soup.find('div', attrs={'class':'_3ZV2G m3_2T _9EVz3 _2CNUL wnn-Y'})
# heading = soup.find('h1').text+' - free download'
# title = heading+' | unity free paid assets'
# soup = soup.find('div',attrs={'class':'_2nw25'})
# size = soup.find('div',attrs={'class':'_27124 product-size'}).text.split('File size')[1] 
# version = soup.find('div',attrs={'class':'_27124 product-version'}).text.split('Latest version')[1]  
# support_version = soup.find('div',attrs={'class':'_27124 product-support_version'}).text.split('Supported Unity versions')[1]  
# url=heading.replace('  ',' ').replace(' ','-').replace('--','-').replace('--','-')
# print(str(soupdes))
# soup = soup.find_all("table")[0].find('a').get('href')
# print(soup)
# print(soup.find('img').get('src'))


# x = ['212 **', "how ** to download", '** presave']
# import random
# random.shuffle(x)
# x = [x.replace('**', 'query') for x in x]
# print(x)


# #
# test


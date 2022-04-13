# click and download all txt files
# http://web.mta.info/developers/turnstile.html

# following tutorial
# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460

# answer we inspected the website and seen 
# all a tag has a download link
# <a href="data/nyct/turnstile/turnstile_220226.txt">Saturday, February 26, 2022</a>

import requests as req
import urllib.request
import time
from bs4 import BeautifulSoup as bs
from HackerGprat import basic as b

url =  "http://web.mta.info/developers/turnstile.html"

response = req.get(url)
print( response.status_code )   # 200 = success

soup = bs( response.text, 'html.parser' )
# print( soup )

allLinks = soup.findAll('a')
# b.viewList(allLinks)
# print( allLinks )

# get only text from all links text
# for i in allLinks:
#     print(i.get_text())   


# extract all link which contain href
one_a_tag = soup.findAll('a')[37]
print( one_a_tag )
print( one_a_tag.get_text() )

download_url = 'http://web.mta.info/developers/'
a = urllib.request.urlretrieve( download_url, './' + link[ link.find('/turnstile_')+1: ] )
time.sleep(1)
print(a)



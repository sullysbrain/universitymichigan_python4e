import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
tags2 = soup('h1')
for tag2 in tags2:
    print(tag2)
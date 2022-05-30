# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#SAMPLE URL
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#ACTUAL URL
url = 'http://py4e-data.dr-chuck.net/known_by_Sweet.html'

# url = input('Enter URL: ')
count = int(input('Enter Count: '))
pos = int(input('Enter Position: '))

while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[pos-1].get('href',None)
    print("Count: " + str(count) + "  Newlink: " + url)
    count = count - 1


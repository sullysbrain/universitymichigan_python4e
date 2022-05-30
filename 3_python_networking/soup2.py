import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Test Data
# url = 'http://py4e-data.dr-chuck.net/comments_42.html'
# Actual Data
url = 'http://py4e-data.dr-chuck.net/comments_1564275.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

commentTotal = 0
tags = soup('span')
for tag in tags:
    x = tag.contents[0]
    commentTotal = commentTotal + int(x)

print(commentTotal)

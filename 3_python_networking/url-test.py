import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

#sample url
# url='http://py4e-data.dr-chuck.net/comments_42.json'
url='http://py4e-data.dr-chuck.net/comments_1564278.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

info = json.loads(data)

count = 0
for item in info['comments']:
    # print('item: ', item['count'])
    count = count + int(item['count'])
print('total:', count)

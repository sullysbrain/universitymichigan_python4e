import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#sample url
# url='http://py4e-data.dr-chuck.net/comments_42.xml'
url='http://py4e-data.dr-chuck.net/comments_1564277.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')

# print('User count:', len(lst))
count = 0
for item in lst:
    # print('name: ', item.find('name').text)
    # print('Count: ', item.find('count').text)
    x = int(item.find('count').text)
    count = count + x
print('total:', count)

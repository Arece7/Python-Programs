import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

numbers = list()
url = input('Enter - ')
#to read the xml data
data = urllib.request.urlopen(url, context=ctx).read()
#converting the data into a tree
tree = ET.fromstring(data)
#use an XPath selector string to look through the entire tree of XML for any tag named 'count'
counts = tree.findall('.//count')
for count in counts:
    num = int(count.text)
    numbers.append(num)
print('total sum :', sum(numbers))
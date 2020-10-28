import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

counts = list()
numbers = list()
while True:
    url = input('Enter - ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    js = json.loads(data)
   
    counts = js['comments']
    for count in counts:
        number = int(count['count'])
        numbers.append(number)

    print('total sum :', sum(numbers))
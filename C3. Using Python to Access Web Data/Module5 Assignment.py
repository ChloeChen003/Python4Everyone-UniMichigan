import urllib.request as ur
import xml.etree.ElementTree as et

url = input('Enter location: ')

num = 0
sum = 0

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    num += 1

print('Count:', num)
print('Sum:', sum)

# http://py4e-data.dr-chuck.net/comments_42.xml 
# http://py4e-data.dr-chuck.net/comments_2148026.xml 
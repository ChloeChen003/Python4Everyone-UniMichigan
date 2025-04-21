import urllib.request
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count):
    print('Retrieving:', url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position - 1].get('href')

print('Last Url:', url)

# http://py4e-data.dr-chuck.net/known_by_Fikret.html
#count 4 / position 3

# http://py4e-data.dr-chuck.net/known_by_Karson.html
# count 7 / position 18 


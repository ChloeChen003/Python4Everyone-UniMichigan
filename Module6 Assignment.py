# del input
import json
import urllib.request as ur

url = input("Enter location: ")
data = ur.urlopen(url).read().decode('utf-8')
obj = json.loads(data)

print("Retrieving", url)
print('Retrieved', len(data), 'characters')

total = 0
count = 0

for comment in obj["comments"]:
    total += int(comment["count"])
    count += 1

print('Count:', count)
print('Sum:', total)

# http://py4e-data.dr-chuck.net/comments_2148027.json
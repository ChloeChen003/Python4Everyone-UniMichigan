import json
import urllib.request, urllib.parse

serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"
address = input("Enter location: ")
params = {'q': address}
url = serviceurl + urllib.parse.urlencode(params)

print("Retrieving", url)

data = urllib.request.urlopen(url).read().decode()
print("Retrieved", len(data), "characters")

js = json.loads(data)
plus_code = js['features'][0]['properties']['plus_code']
print("Plus code", plus_code)
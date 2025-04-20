import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# API endpoint
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# Prompt for a location
address = input('Enter location: ')

# Prepare parameters for the API request
params = dict()
params['q'] = address

# Encode the parameters and create the complete URL
url = serviceurl + urllib.parse.urlencode(params)
print('Retrieving', url)

# Make the request and read the response
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    # Parse the JSON data
    js = json.loads(data)
except:
    js = None

# Check if we have valid data
if not js or 'features' not in js or len(js['features']) == 0:
    print('==== Failure To Retrieve ====')
    print(data)
    exit()

# Extract the plus_code from the first feature
plus_code = js['features'][0]['properties']['plus_code']
print('Plus code', plus_code)
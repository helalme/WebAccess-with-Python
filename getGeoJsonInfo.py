import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter location: ')
parms = {'address': address, 'key':42}
url = 'http://py4e-data.dr-chuck.net/json?' + urllib.parse.urlencode(parms)
uh = urllib.request.urlopen(url)
js = json.loads(uh.read().decode())

print(json.dumps(js, indent=4))

'''
lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)
'''
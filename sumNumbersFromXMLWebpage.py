import xml.etree.ElementTree as ET
import urllib.request

response = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_769621.xml').read()
tree = ET.fromstring(response)
print(sum(int(i.text) for i in tree.findall('.//count')))
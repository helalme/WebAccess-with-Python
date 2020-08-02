import urllib.request, urllib.parse, json

uh = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_769622.json")
info = json.loads(uh.read().decode())
print(sum([int(item['count']) for item in info['comments']]))
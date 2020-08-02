from urllib.request import urlopen
from bs4 import BeautifulSoup

soup = BeautifulSoup(urlopen("http://py4e-data.dr-chuck.net/comments_769619.html").read(), "html.parser")
print(sum([int(tag.text) for tag in soup('span')]))

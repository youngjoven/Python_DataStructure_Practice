# download source requests and bs4
import requests
from bs4 import BeautifulSoup

r=requests.get("http://joven.design/dig.html")
c=r.content

# print(c) this will be hard to read, so html.parser is required
# It is more clear
soup=BeautifulSoup(c, "html.parser")
#print(soup)

all=soup.find("body")
print(all)


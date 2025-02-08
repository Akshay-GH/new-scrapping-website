import requests
from bs4 import BeautifulSoup

url ="https://edition.cnn.com/"
r = requests.get("https://edition.cnn.com/")
soup = BeautifulSoup(r.content, 'html5lib') 


items =soup.find_all('span', attrs = {'data-editable':'headline'})

for item in items:
    print(item.text)


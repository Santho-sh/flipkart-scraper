import requests
from bs4 import BeautifulSoup
import json

f = open('output.json')
data = json.load(f)

for i in data:
    link = i["link"]
    old_price = i["price"]

    r = requests.get(link)

    soup = BeautifulSoup(r.content, 'html5lib')

    price = soup.find('div', attrs={"class": "_16Jk6d"}).text

    price = int(price[1:].replace(",", ""))

    print(price, old_price)
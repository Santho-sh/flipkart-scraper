import requests
import json
from bs4 import BeautifulSoup
import time
from colorama import Fore, Style
import re
import math


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

url = "https://www.flipkart.com/search?q=Redmi%20A1&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


flipkart = "https://www.flipkart.com/"

with open("search.json", "r") as file:
    mobiles = json.load(file)

mobile = "Redmi A1"

def get_price():

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')
    # extract price using class '_16Jk6d'
    all_name = soup.find_all("div", attrs={"class": "_4rR01T"})
    all_price = soup.find_all("div", attrs={"class": "_30jeq3"})
    all_links = soup.find_all("a", attrs={"class": "_1fQZEK"})

    lowest_price = math.inf
    link = ""

    for i in range(len(all_name)):

        if match := re.search(r"(.+) \(.+", all_name[i].text, re.IGNORECASE):
            
            name = match.group(1).lower()
            if name == mobile.lower():
                price = all_price[i].text
                # remove Rs symbol from price
                price = price[1:]
                # remove commas from price
                price = int(price.replace(",", ""))

                if price < lowest_price:
                    lowest_price = price
                    link = all_links[i]["href"]
                    
            else:
                continue
 
    return lowest_price, f"https://www.flipkart.com{link}"
    
price, link = get_price()

print(price)
print(link)

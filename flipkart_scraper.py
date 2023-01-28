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


def get_price():

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')
    # extract price using class '_16Jk6d'
    all_name = soup.find_all("div", attrs={"class": "_4rR01T"})
    all_price = soup.find_all("div", attrs={"class": "_30jeq3"})

    lowest_price = math.inf

    for i in range(len(all_name)):

        if match := re.search(r"(.+) \(.+", all_name[i].text, re.IGNORECASE):
            
            name = match.group(1).lower()
            if name == mobile.lower():
                price = all_price[i].text
                # remove Rs symbol from price
                price = price[1:]
                # remove commas from price
                price = price.replace(",", "")
                # contvert price into integer
                price = int(price)

                if price < lowest_price:
                    lowest_price = price
                    
            else:
                continue
    return lowest_price
    
price = get_price()

print(price)

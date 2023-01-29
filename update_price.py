import requests
from bs4 import BeautifulSoup

link = "https://www.flipkart.com/redmi-a1-light-green-32-gb/p/itmc25a41ed1907d?pid=MOBGHFFT4DJHDZEQ&lid=LSTMOBGHFFT4DJHDZEQZQAXJ3&marketplace=FLIPKART&q=redmi+a1&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&fm=organic&iid=5a88c0e7-b79f-4460-96a6-35a22a7edbe1.MOBGHFFT4DJHDZEQ.SEARCH&ppt=None&ppn=None&ssid=inumkndf4w0000001674986158449&qH=d5781f611e5744f0"

r = requests.get(link)

soup = BeautifulSoup(r.content, 'html5lib')

price = soup.find('div', attrs={"class": "_16Jk6d"}).text

price = int(price[1:].replace(",", ""))

print(price)
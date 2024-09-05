import requests
from bs4 import BeautifulSoup as BS

city = {"Navoiy":"погода-навои", "Andijon":"погода-андижан", "Samarqand":"погода-самарканд", "Toshkent": "погода-ташкент","Guliston":"погода-гулистан",
        "Buxoro": "погода-бухара","Qarshi":"погода-карши"}



def ob_havo(city):
    t = requests.get(f"https://sinoptik.ua/{city}")
    html_t = BS(t.content,"html.parser")
    for el in html_t.select('#content'):
        min = el.select('.temperature .min') [0].text
        max = el.select('.temperature .max') [0].text
        return min,max


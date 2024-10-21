from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

url = "https://habr.com/ru/articles/544828/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
soup.find_all('code')
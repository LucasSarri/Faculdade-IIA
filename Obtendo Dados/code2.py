from bs4 import BeautifulSoup
import requests


html = requests.get("http://www.example.com").text
print(html)
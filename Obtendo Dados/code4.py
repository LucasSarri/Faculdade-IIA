#https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.94fmdourados.com.br/noticias").text
soup = BeautifulSoup(html, 'html5lib')

artigoss =[]

noticias = soup.find_all('h2',{'class':'title'})

for a in noticias:
    print(a.text)
